import { seasonData } from "../../../data/season_data";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState, useContext } from "react";
import { addToList, getListThunk } from "../../redux/list";
import { getPlayerPosts, deletePost } from "../../redux/post";
import { getLikesThunk, addLikeThunk, removeLikeThunk, clearLikes } from "../../redux/like";
import OpenModalButton from "../OpenModalButton";
import PostModal from "./PostModal";
import { MyContext } from "../../router/Layout";
import { useNavigate } from "react-router-dom";

const PlayerPage = (props) => {
  const { playerData } = props;
  const { player, year, selectYear } = useContext(MyContext); 
  const user = useSelector(state => state.session.user);
  const list = useSelector(state => state.list.list);
  let posts = useSelector(state => state.posts.playerPosts);
  const playerLikes = useSelector(state => state.likes.playerLikes);
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  const navigate = useNavigate()

  if(!year) selectYear(2023) 
  const selectedPlayer = playerData[player]
  
  useEffect (() => {
    if(!player) navigate('/')
      dispatch(getPlayerPosts(player))
      .then(() => dispatch(clearLikes()))
      .then(() => dispatch(getListThunk()))
      .then(() => dispatch(getLikesThunk(player)))
      .then(() => setIsLoaded(true))
  }, [dispatch, player, navigate])
  
  const handleAdd = e => {
    e.preventDefault()
    dispatch(addToList(player))
  }

  const handleDelete = postId => e => {
    e.preventDefault()
    dispatch(deletePost(postId))
    .then(() => dispatch(getPlayerPosts(player)))
  }

  const handleLike = e => {
    e.preventDefault()
    if(playerLikes[user.id]) {
      dispatch(removeLikeThunk(player))
      .then(() => dispatch(getLikesThunk(player)))
    } else {
      dispatch(addLikeThunk(player))
      .then(() => dispatch(getLikesThunk(player)))
    }
  }

   const handleChange = e => {
      selectYear(e.target.value)
    };

  if (isLoaded) {
    if (posts) posts = Object.values(posts) 
    const stats = selectedPlayer.seasons.find(s => s.year == year).teams[0]

  return (
    <main>
      <h1>{selectedPlayer.full_name}</h1>
      <h2>{Object.values(playerLikes).length} likes</h2>
      {user && 
      <button className='btn' onClick={handleLike}>Like</button>}
      <h3>Position: {selectedPlayer.position}, Current Team: {selectedPlayer.team? selectedPlayer.team.name: 'Not Currently in NBA'}, Drafted: {selectedPlayer.draft.year} Rd {selectedPlayer.draft.round} Pk {selectedPlayer.draft.pick}, Years Pro: {selectedPlayer.seasons[0].year - selectedPlayer.draft.year + 1}</h3>
      {user && list && !Object.values(list).find(p => p == selectedPlayer.id) &&
        <button className="btn" onClick={handleAdd}>Add to top 5</button>}
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
                    <td>{seasonData[year].categories[2].ranks.find(rank => rank.player.id == player)? seasonData[year].categories[2].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[3].ranks.find(rank => rank.player.id == player)? seasonData[year].categories[3].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[0].ranks.find(rank => rank.player.id == player)? seasonData[year].categories[0].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[1].ranks.find(rank => rank.player.id == player)? seasonData[year].categories[1].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[5].ranks.find(rank => rank.player.id == player)? seasonData[year].categories[5].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[4].ranks.find(rank => rank.player.id == player)? seasonData[year].categories[4].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[6].ranks.find(rank => rank.player.id == player)? seasonData[year].categories[6].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{seasonData[year].categories[7].ranks.find(rank => rank.player.id == player)? seasonData[year].categories[7].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                </tr>
            </tbody>
        </table>
        <label htmlFor='year-select'>Select a season</label>
      <select name='year' id='year-select' onChange={handleChange} defaultValue={2023}>
        {selectedPlayer.seasons.filter((season) => season.type == 'REG').map(s => {
          return (
            <option value={s.year} key={s.year}>{s.year}</option>
          )
        })}
      </select>  
      </div>
      <div className="card">
        <h2>Posts</h2>
        {user &&
        <OpenModalButton
        modalComponent={<PostModal method={'POST'}/>}
        buttonText={'write a post'}
        onModalClose={(() => dispatch(getPlayerPosts(player.id)))} 
        />}
        {posts &&
        <ul>{posts.map(post => {
          const created = new Date(post.created_at)
          return (
          <li key={post.id}  className="card">
            <h3>{post.title} {post.updated_at != post.created_at && "(edited)"}</h3>
            <p>By: {post.username}</p>
            <p>On: {created.toDateString()}</p>
            <p>{post.body}</p>
            {user && user.id == post.user_id && 
              <OpenModalButton
              modalComponent={<PostModal method={'PUT'} postId={post.id}/>}
              buttonText={'edit post'}
              onModalClose={(() => dispatch(getPlayerPosts(player.id)))} 
              />}
            {user && user.id == post.user_id && 
              <button className="btn" onClick={handleDelete(post.id)}>delete post</button>}
          </li>
        )})}
        </ul>}
        {!Object.keys(posts).length &&
        <p>No posts yet</p>}
      </div> 
    </main>
  )
    } else return (<p>Player not found</p>)
};

export default PlayerPage;
