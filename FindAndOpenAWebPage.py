from random import randint

from selenium import webdriver

"""
This class allows to open google chrome, search a web site thanks to 
Google. On google, a method can search the web site on the pages of google
if the web site is on the page it can open it. And there is another that 
allows to go to the next page of google to find the web site. And in the 
web site, it will surf on it like a user.
@author: Kierian Tirlemont
"""


class FindAndOpenAWebPage:
    """
    Constructor of the class which initializes the attributes.
    """

    def __init__(self, webSiteName, searchName):
        self.driver = webdriver.Chrome()
        self.webSiteName = webSiteName
        self.searchName = searchName
        self.intCurrentPage = 1

    """
    Launch the required methods that launch the application.
    """

    def mainApp(self):
        endSearch = True
        FindAndOpenAWebPage.search(self)
        while endSearch:
            if not FindAndOpenAWebPage.findAndOpenWebSite(self):
                if self.intCurrentPage == 11:
                    endSearch = False
                endSearch = FindAndOpenAWebPage.nextPage(self)
            else:
                endSearch = False
                FindAndOpenAWebPage.navigationOnTheWebSite(self)
        #self.driver.close()

    """
    Open google and search the search name.
    """

    def search(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_xpath("//input[@name=\"q\"]").send_keys(self.searchName)
        # Make possible to click to search by enable the current selection
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div[2]/div[1]/div/a').click()
        # click on search
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div[1]/div[3]/center/input[1]').click()

    """
    This method allows to lock at every links on the page. If one of
    the link corresponds to the web site name, it opens it else it does
    nothing. 
    """

    def findAndOpenWebSite(self):
        elems = self.driver.find_elements_by_tag_name('a')

        for elem in elems:
            href = elem.get_attribute('href')
            if href is not None:
                if href == self.webSiteName:
                    exist = True
                    elem.click()
                    # need to stop the loop
                    return True
        return False

    """
    This method allows to go to the next page of google.
    """

    def nextPage(self):
        elems = self.driver.find_elements_by_tag_name('a')
        nextPage = "Page " + str(self.intCurrentPage + 1)
        # print(nextPage)
        for elem in elems:
            href = elem.get_attribute('href')
            if href is not None:
                if elem.get_attribute('class') == 'G0iuSb':
                    if elem.get_attribute('id') == 'pnnext':
                        elem.click()
                        self.intCurrentPage += 1
                        # need to stop the loop
                        return True
        return False

    """
    End of the application.
    """

    def end(self):
        exit()

    """
   This method allows to navigate on the website in the main tab of the site. 
    """

    def navigationOnTheWebSite(self):
        tabWebSite = []
        tabWebSite.append(self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[2]/div/nav[1]/ul/li[1]/a'))
        tabWebSite.append(self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[2]/div/nav[1]/ul/li[2]/a'))
        tabWebSite.append(self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[2]/div/nav[1]/ul/li[3]/a'))
        tabWebSite.append(self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[2]/div/nav[1]/ul/li[4]/a'))
        tabWebSite.append(self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[2]/div/nav[1]/ul/li[5]/a'))
        tabWebSite.append(self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[2]/div/nav[1]/ul/li[6]/a'))

        continu = 0
        while continu == 0:
            action = randint(0, 5)
            toDo = tabWebSite[action]
            toDo.click()
            continu = randint(0, 2)