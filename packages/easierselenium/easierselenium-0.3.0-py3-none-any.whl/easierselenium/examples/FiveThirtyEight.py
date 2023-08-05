"""
Script to retrieve sports game odds from www.fivethirtyeight.com
"""
#####################################
#       Imports                     #
#####################################

from datetime import datetime
import pandas as pd
from easierselenium import BaseWebInteractor
from selenium.webdriver.common.by import By

#####################################
#       FiveThirtyEightInteractor   #
#####################################


class FiveThirtyEightInteractor(BaseWebInteractor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DOMAIN = "https://projects.fivethirtyeight.com"

    def get_dutch_soccer_odds(self):
        BASE_URL = "https://projects.fivethirtyeight.com/soccer-predictions/eredivisie/"
        self.driver.get(BASE_URL)
        # Navigate to correct view
        nav_toggle = self.find(by=By.ID, identifier="js-nav-toggle")
        matches_button = nav_toggle.find_element(
            By.XPATH, "//label[@for='toggle-matches']"
        )
        matches_button.click()
        more_upcoming_button = self.find(
            by=By.CSS_SELECTOR, identifier=".more-upcoming.btn-cta"
        )
        more_upcoming_button.click()
        match_containers_parent = self.find(
            by=By.CSS_SELECTOR, identifier=".games-container.upcoming"
        )
        match_containers = match_containers_parent.find_elements(
            By.CSS_SELECTOR, ".match-container"
        )
        # Get the league info
        league_info = self.find(by=By.CSS_SELECTOR, identifier=".league-info")
        league_name = league_info.find_element(By.CSS_SELECTOR, ".leagueName").text
        league_season = league_info.find_element(By.CSS_SELECTOR, ".leagueDate").text
        league_country = league_info.find_element(
            By.CSS_SELECTOR, ".leagueCountry"
        ).text
        # Get date odds were updated
        timestamp_odds_updated = league_info.find_element(
            By.CSS_SELECTOR, ".timestamp"
        ).text
        timestamp_odds_updated_parsed = self.timestamp_updated_to_datetime(
            timestamp_odds_updated
        )
        # Create matches dataframe
        matches = []
        for match_container in match_containers:
            match_info = self.get_match_info(match_container)
            match_info["league_name"] = league_name
            match_info["league_season"] = league_season
            match_info["league_country"] = league_country
            match_info["timestamp_odds_updated"] = timestamp_odds_updated_parsed
            matches.append(match_info)
        matches_df = pd.DataFrame(matches)
        return matches_df

    def timestamp_updated_to_datetime(self, timestamp_updated):
        """timestamp is of the form 'Updated Month Day, Year, at HH:MM p.m.'"""
        month, day, year = timestamp_updated.split(" ")[1:4]
        year = year.strip(",")
        is_am = timestamp_updated.split(" ")[-1].startswith("a")
        hour, minute = timestamp_updated.split(" ")[-2].split(":")
        if not is_am:
            hour = int(hour) + 12
        return pd.to_datetime(f"{year}-{month}-{day} {hour:02}:{minute}")

    def percent_to_float(self, percent):
        return float(percent.strip("%")) / 100

    def match_date_to_date(self, match_date):
        """match_date is of the form month/day"""
        month, day = match_date.split("/")
        year = datetime.now().year
        return pd.to_datetime(f"{year}-{month}-{day}")

    def get_match_info(self, match_container):
        match_info = {}
        match_info["match_date"] = self.match_date_to_date(
            match_container.find_element(By.CSS_SELECTOR, ".date")
            .find_element(By.TAG_NAME, "div")
            .text
        )
        match_info["team_one"] = match_container.get_attribute("data-team1")
        match_info["team_two"] = match_container.get_attribute("data-team2")
        match_info["team_one_odds"] = self.percent_to_float(
            match_container.find_element(By.CSS_SELECTOR, ".match-top")
            .find_element(By.CSS_SELECTOR, ".prob")
            .text
        )
        match_info["team_two_odds"] = self.percent_to_float(
            match_container.find_element(By.CSS_SELECTOR, ".match-bottom")
            .find_element(By.CSS_SELECTOR, ".prob")
            .text
        )
        match_info["draw_odds"] = self.percent_to_float(
            match_container.find_element(By.CSS_SELECTOR, ".tie-prob")
            .find_element(By.TAG_NAME, "div")
            .text
        )
        return match_info


#####################################
#       Main                        #
#####################################


if __name__ == "__main__":
    interactor = FiveThirtyEightInteractor(headless=False)
    matches_df = interactor.get_dutch_soccer_odds()
    print(matches_df.iloc[1])
