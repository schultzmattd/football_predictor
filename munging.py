from robobrowser import RoboBrowser

def get_scores(year, week):

    pfr_url = "http://www.pro-football-reference.com/years/{}/week_{}.htm".format(year, week)
    scores = {"week":[],"game_number":[],"year":[],"team":[],"points":[]}
    browser = RoboBrowser()
    browser.open(pfr_url)

    for game_number, team_table in enumerate(browser.find_all("table",{"class":"teams"})):
        table_cells = team_table.find_all("td")
        first_team_name = str(table_cells[1].string)
        first_team_points = int(table_cells[2].contents[0])

        second_team_name = str(table_cells[4].string)
        second_team_points = int(table_cells[5].contents[0])

        scores["week"].append(week)
        scores["year"].append(year)
        scores["team"].append(first_team_name)
        scores["points"].append(first_team_points)
        scores["game_number"].append(game_number)

        scores["week"].append(week)
        scores["year"].append(year)
        scores["team"].append(second_team_name)
        scores["points"].append(second_team_points)
        scores["game_number"].append(game_number)

    return scores

if __name__ == '__main__':
    get_scores(2016,1)