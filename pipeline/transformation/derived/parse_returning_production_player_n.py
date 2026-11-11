from pipeline.scrapers.derived.returning_production_player_n import fetch_returning_production_player_n

def parse_returning_production_player_n(raw_returning_production_player): 
    list_returning_production_player_n = []

    for i_returning_production_player in raw_returning_production_player: 

        # function in order to keep the column in missing value
        def missing_value_player_n(val_missing_value_player_n): 
            return i_returning_production_player.get(val_missing_value_player_n, 0)

        dict_returning_production_player_n = {
            "player_id": i_returning_production_player["player_id"], 
            "team": i_returning_production_player["team"], 
            "season": i_returning_production_player["season"], 
            # passing
            "returning_passing_yards": missing_value_player_n("passing_yards"), 
            "returning_passing_touchdowns": missing_value_player_n("passing_touchdowns"),
            "returning_passing_attempts": missing_value_player_n("passing_attempts"),
            "returning_passing_completions": missing_value_player_n("passing_completions"),
            "returning_passing_interceptions": missing_value_player_n("passing_interceptions"),
            # rushing
            "returning_rushing_yards": missing_value_player_n("rushing_attempts"), 
            "returning_rushing_touchdowns": missing_value_player_n("rushing_touchdowns"), 
            "returning_rushing_attempts": missing_value_player_n("rushing_attempts"), 
            # receiving
            "returning_receiving_yards": missing_value_player_n("receiving_yards"),
            "returning_receiving_touchdowns": missing_value_player_n("receiving_touchdowns"),
            "returning_receiving_receptions": missing_value_player_n("receiving_receptions"),
            # tackles , sacks, qb_hurries, passes, assisted
            "returning_tackles": missing_value_player_n("tackles"), 
            "returning_solo_tackles": missing_value_player_n("solo_tackles"), 
            "returning_assisted_tackles": missing_value_player_n("assisted_tackles"), 
            "returning_sacks": missing_value_player_n("sacks"), 
            "returning_qb_hurries": missing_value_player_n("qb_hurries"),
            "returning_passes_defended": missing_value_player_n("passes_defended"), 
            # ftl
            "returning_tackles_for_loss": missing_value_player_n("tackles_for_loss"), 
            # fg_made , fg_attempted
            "returning_fg_made": missing_value_player_n("fg_made"), 
            "returning_fg_attempted": missing_value_player_n("fg_attempted"),
            # xp_made , xp_attempted
            "returning_xp_made": missing_value_player_n("xp_made"), 
            "returning_xp_attempted": missing_value_player_n("xp_attempted"), 
            # punt
            "returning_punt_yards": missing_value_player_n("punt_yards"),
            "returning_punt_long":missing_value_player_n("punt_long"),
            "returning_punt_attempts": missing_value_player_n("punt_attempts"), 
            # kick
            "returning_kick_returns_yards": missing_value_player_n("kick_returns_yards"), 
            "returning_kick_returns_touchdowns": missing_value_player_n("kick_returns_touchdowns"), 
            # punt
            "returning_punt_returns_yards": missing_value_player_n("punt_returns_yards"), 
            "returning_punt_returns_touchdowns": missing_value_player_n("punt_returns_touchdowns")

        }

        list_returning_production_player_n.append(dict_returning_production_player_n)

    return list_returning_production_player_n
