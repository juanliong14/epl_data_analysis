def get_data(match_id, file_name):

    '''
    created on Saturday, 19 June 2021
    author : Juan Liongnardo
    
    '''

    from datetime import datetime
    #get start time to count for run duration
    start_time = datetime.now()

    #import libraries
    import os
    import time 
    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException, TimeoutException

    #get working directory path
    wd = os.getcwd()

    #declare web driver path
    path = wd + '\geckodriver' 
    driver = webdriver.Firefox(executable_path=path)

    #blank list for EPL data
    epl_data = []

    #counter definition
    counter = 1

    for id in match_id:

        #sending get request
        url = 'https://www.premierleague.com/match/' + str(id)
        driver.get(url)

        #for the first visit only
        if counter == 1:
            try:
                #wait until accept cookies is clickable
                time.sleep(10)
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary.cookies-notice-accept")))
                
                element.click()
                print('accept cookies button is clicked')
            except TimeoutException:
                print('element not found, time out')
                pass
        
        time.sleep(5)

        #scrap the basic info of the match
        match_date = driver.find_element_by_class_name('matchDate.renderMatchDateContainer').text
        match_week = driver.find_element_by_xpath('/html/body/main/div/header/div[3]/div[2]/div[1]').text
        home_team = driver.find_element_by_class_name('team.home').text
        away_team = driver.find_element_by_class_name('team.away').text
        score = driver.find_element_by_class_name('score.fullTime').text

        #click match stats tab
        try:
            #scroll page for 150 px
            driver.execute_script("window.scrollTo(0, 150)")
            print('scrolling success')

            #find and click match stats tab
            match_stats_tab = driver.find_element_by_xpath('//ul[@class="tablist"]/li[@data-tab-index="2"]')
            match_stats_tab.click()
            print('match stats button is clicked ')
        except NoSuchElementException:
            print('element not found')
            pass

        #scroll page for 550 px
        driver.execute_script("window.scrollTo(0, 550)")
        time.sleep(10)

        #scrap match stats
        try:
            possession = driver.find_element_by_xpath('//tbody[@class="matchCentreStatsContainer"]//tr[1]').text
        except NoSuchElementException:
            possession = -1
        
        try:
            shots_on_target = driver.find_element_by_xpath('//tbody[@class="matchCentreStatsContainer"]//tr[2]').text
        except NoSuchElementException:
            shots_on_target = -1
        
        try:
            shots = driver.find_element_by_xpath('//tbody[@class="matchCentreStatsContainer"]//tr[3]').text
        except NoSuchElementException:
            shots = -1


        print('Data Scrapped Successfully, Progress ' + str(counter) + '/' + str(len(match_id)))
        counter += 1

        epl_data.append({'match_id':id,
        'match_date':match_date,
        'matchweek': match_week,
        'home_team':home_team,
        'away_team':away_team,
        'score':score,
        'possession':possession,
        'shots_on_target':shots_on_target,
        'shots':shots
        })


    df = pd.DataFrame(epl_data)
    file = df.to_csv(file_name + '.csv')
    print('File created successfully')
    
    driver.quit()

    #calculate and print run duration
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    
    return(file)



