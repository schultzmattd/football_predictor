import pandas

from robobrowser import RoboBrowser


def get_scores_year_range(start_year, end_year):
    scores = {"week": [], "game_number": [], "year": [], "team": [], "points": [], "points_for_per_game": [],
              "points_against_per_game": []}

    cumulative_points_for = {}
    cumulative_points_against = {}
    for year in range(start_year, end_year + 1):
        for week in range(1, 18):
            pfr_url = "http://www.pro-football-reference.com/years/{}/week_{}.htm".format(year, week)

            browser = RoboBrowser()
            browser.open(pfr_url)

            for game_number, team_table in enumerate(browser.find_all("table", {"class": "teams"})):
                table_cells = team_table.find_all("td")
                first_team_name = str(table_cells[1].string)
                first_team_points = int(table_cells[2].contents[0])

                second_team_name = str(table_cells[4].string)
                second_team_points = int(table_cells[5].contents[0])

                if first_team_name not in cumulative_points_for:
                    scores["points_for_per_game"].append("NA")
                    scores["points_against_per_game"].append("NA")

                    cumulative_points_for[first_team_name] = first_team_points
                    cumulative_points_against[first_team_name] = second_team_points
                else:
                    scores["points_for_per_game"].append(cumulative_points_for[first_team_name] / (week - 1))
                    scores["points_against_per_game"].append(cumulative_points_against[first_team_name] / (week - 1))

                    cumulative_points_for[first_team_name] += first_team_points
                    cumulative_points_against[first_team_name] += second_team_points

                if second_team_name not in cumulative_points_for:
                    scores["points_for_per_game"].append("NA")
                    scores["points_against_per_game"].append("NA")

                    cumulative_points_for[second_team_name] = second_team_points
                    cumulative_points_against[second_team_name] = first_team_points
                else:
                    scores["points_for_per_game"].append(cumulative_points_for[second_team_name] / (week - 1))
                    scores["points_against_per_game"].append(cumulative_points_against[second_team_name] / (week - 1))

                    cumulative_points_for[second_team_name] += second_team_points
                    cumulative_points_against[second_team_name] += first_team_points

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
    # start_year = 2000
    start_year = 2016
    end_year = 2016

    scores = get_scores_year_range(start_year, end_year)

    data_frame = pandas.DataFrame(scores)
    data_frame.to_csv("data/scores_{}_{}.csv".format(start_year, end_year), index=False)
