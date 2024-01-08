from requests import get


def gov():
    '''
    Gets live covid updates from www.moh.gov.sg, note, these are new cases

    :return: tuple(date, artCount, pcrCount, totalCount, "https://www.gov.sg/features/covid-19")
    '''

    def fetch_result():
        moh_url = "https://www.gov.sg/features/covid-19"
        response = get(moh_url)

        return response.text

    html = fetch_result()

    caseStart = html.find('<span style="font-family: Arial; font-size: 24px; color: #000000;">')
    caseEnd = html[caseStart + 1:].find('<span style="font-family: Arial; font-size: 24px; color: #000000;">')

    caseSummary = html[caseStart: caseStart + caseEnd]

    dateStart = caseSummary.find('as of')
    dateEnd = caseSummary.find('</span></strong></span></strong><strong style="font-size: 13px;">')

    date = caseSummary[dateStart + 6: dateEnd]

    pcrStart = caseSummary.find('<span style="font-family: Arial; font-size: 24px; color: #008080;"><strong>')
    pcrEnd = caseSummary[pcrStart:].find('</strong></span></td>')
    pcrCount = caseSummary[pcrStart + 75: pcrEnd + pcrStart]

    if ',' in pcrCount:
        pcrCount = int(pcrCount.replace(',', ''))


    artStart = caseSummary[pcrEnd:].find('<span style="font-size: 24px; color: #008080;"><strong>')
    artEnd = caseSummary[artStart:].find('</strong></span></td>')
    artCount = caseSummary[artStart + 135: artStart + artEnd]
    
    if ',' in artCount:
        artCount = int(artCount.replace(',', ''))


    totalCount = artCount + pcrCount

    return (date, artCount, pcrCount, totalCount, "https://www.gov.sg/features/covid-19")
