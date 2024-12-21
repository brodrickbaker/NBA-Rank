import { useParams } from "react-router-dom";
import { seasonData } from "../../../data/season_data";
import { useSelector, useDispatch } from "react-redux";
import { useEffect } from "react";
import { setPlayer } from "../../redux/selected";
import { addToList } from "../../redux/list";
import { getListThunk } from "../../redux/list";

const PlayerPage = (props) => {
  const { playerData } = props
  const { playerId } = useParams()  
  const player = playerData[playerId]
  const user = useSelector(state => state.session.user);
  const year = useSelector(state => state.selected.year)? useSelector(state => state.selected.year): 2023
  const list = useSelector(state => state.list.list)
  const dispatch = useDispatch()

  useEffect (() => {
    dispatch(setPlayer(player?.full_name))
    dispatch(getListThunk())
  }, [dispatch])
  
  const handleClick = (e) => {
    e.preventDefault()
    dispatch(addToList(playerId))
  }

  if (player) {
  
  const stats = player.seasons.find(season => season.year == year).teams[0]

  return (
    <main>
      <h1>{player.full_name}</h1>
      <h3>Position: {player.position}, Current Team: {player.team? player.team.name: 'Not Currently in NBA'}, Drafted: {player.draft.year} Rd {player.draft.round} Pk {player.draft.pick}, Years Pro: {player.seasons[0].year - player.draft.year + 1}</h3>
      {user && list && !Object.values(list).find(p => p == player.id) &&
        <button className="btn" onClick={handleClick}>Add to top 5</button>}
      <h2>{year}-{Number(year) + 1} Season Stats</h2>
      <div id='stats' className="card">
        <table>
            <thead>
                <tr>
                    <th>Stat Category:</th>
                    <th>Minutes</th>
                    <th>Points</th>
                    <th>FG %</th>
                    <th>Ft %</th>
                    <th>Assists</th>
                    <th>Rebounds</th>
                    <th>Steals</th>
                    <th>Blocks</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th>Avg:</th>
                    <td>{stats.average.minutes}</td>
                    <td>{stats.average.points}</td>
                    <td>{(stats.total.field_goals_pct*100).toFixed(1)}</td>
                    <td>{(stats.total.free_throws_pct*100).toFixed(1)}</td>
                    <td>{stats.average.assists}</td>
                    <td>{stats.average.rebounds}</td>
                    <td>{stats.average.steals}</td>
                    <td>{stats.average.blocks}</td>

                </tr>
                <tr>
                    <th>Rank:</th>
                    <td>{seasonData[year].categories[2].ranks.find(rank => rank.player.id == playerId)? seasonData[year].categories[2].ranks.find(rank => rank.player.id == playerId).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[3].ranks.find(rank => rank.player.id == playerId)? seasonData[year].categories[3].ranks.find(rank => rank.player.id == playerId).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[0].ranks.find(rank => rank.player.id == playerId)? seasonData[year].categories[0].ranks.find(rank => rank.player.id == playerId).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[1].ranks.find(rank => rank.player.id == playerId)? seasonData[year].categories[1].ranks.find(rank => rank.player.id == playerId).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[5].ranks.find(rank => rank.player.id == playerId)? seasonData[year].categories[5].ranks.find(rank => rank.player.id == playerId).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[4].ranks.find(rank => rank.player.id == playerId)? seasonData[year].categories[4].ranks.find(rank => rank.player.id == playerId).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[6].ranks.find(rank => rank.player.id == playerId)? seasonData[year].categories[6].ranks.find(rank => rank.player.id == playerId).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[7].ranks.find(rank => rank.player.id == playerId)? seasonData[year].categories[7].ranks.find(rank => rank.player.id == playerId).rank: "N/R"}</td>
                </tr>
            </tbody>
        </table>
      </div>
      <h2>Posts</h2>
      <div className="card"><p>No posts yet</p></div>
    </main>
  )
    } else return (<p>Player not found</p>)
};

export default PlayerPage;
