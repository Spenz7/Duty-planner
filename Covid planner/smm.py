from requests import get

def fetch_result(url):
    response = get(url)
    return response.text


def workplace():
    '''
    Safe management measures from mom.gov.sg


    '''
    html = fetch_result('https://www.mom.gov.sg/covid-19/requirements-for-safe-management-measures')
    linkStart = html.find('<a rel="noopener noreferrer" class="link--external" href="')
    linkEnd = html[linkStart:].find(' target="_blank">')
    link = html[linkStart + 58: linkStart + linkEnd]
    link = link[:-1]

    return link


print(workplace())


def govupdate():
    '''
    Covid regulation updates from gov.sg

    :type topLink:  str
    :var topLink:   The link to the latest update from moh.gov.sg/covid-19

    :type date:     str
    :var date:      The date of release of the latest update

    :return:        tuple(topLink, date)
    '''

    html = fetch_result('https://www.moh.gov.sg/covid-19')
    linkStart = html.find('<span style="font-size: 16px; font-family: Arial;"><a href="')
    linkEnd = html[linkStart:].find('" title="" class="" target="_blank">')
    topLink = html[linkStart + 60: linkStart + linkEnd]

    dateStart = html.find('</tr><tr><td width="123" class="" style="width: 128px;"><span style="font-size: 16px; font-family: Arial;">')
    dateEnd = html[dateStart:].find('</span>')
    date = html[dateStart + 107: dateStart + dateEnd]

    return (topLink, date)

