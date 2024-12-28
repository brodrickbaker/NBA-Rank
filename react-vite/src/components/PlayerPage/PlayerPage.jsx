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
import { BiLike, BiSolidLike } from "react-icons/bi";

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
  const selectedPlayer = playerData[player]
  let listItems = []
  if(!year || (selectedPlayer && !Object.values(selectedPlayer.seasons).find(season => season.year == year))) selectYear(2023) 

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

  if(!isLoaded) {
    return (
      <h2 style={{textAlign:'center'}}>
      fetching player data
      </h2>
    )
  }

  if (isLoaded && selectedPlayer) {
    if (posts) posts = Object.values(posts) 
    const stats = selectedPlayer.seasons.find(s => s.year == year).teams[0]
    const season = seasonData[year]
    if (list) {
      listItems = Object.values(list).filter(item => item)
    }
  return (
    <main>
      <div className="title">
        <h1>{selectedPlayer.full_name}</h1>
        {user && list && !listItems.find(p => p == selectedPlayer.id) && listItems.length < 6 &&
              <button className="btn" onClick={handleAdd}>Add to top 5</button>}
        <h2>
          {Object.values(playerLikes).length} {Object.values(playerLikes).length == 1? "like":"likes"} &nbsp;
          {user && playerLikes[user.id] &&
          <a onClick={handleLike}><BiSolidLike /></a>}
          {user && !playerLikes[user.id] &&
          <a onClick={handleLike}><BiLike /></a>}
        </h2>
      </div>
      <div id='player-info'>
        <h3>Position: {selectedPlayer.position}</h3>
        <h3>Current Team: {selectedPlayer.team? selectedPlayer.team.name: 'Not Currently in NBA'}</h3>
        <h3>Drafted: {selectedPlayer.draft.year} Rd {selectedPlayer.draft.round} Pk {selectedPlayer.draft.pick}</h3>
        <h3>Years Pro: {selectedPlayer.seasons[0].year - selectedPlayer.draft.year + 1}</h3>
      </div>
      <div id='stats' className="card">
        <div id='season'>
        <h2>{year}-{Number(year) + 1} Season Stats</h2>
        <select name='year' id='year-select' onChange={handleChange} defaultValue='Select a season'>
            <option disabled>Select a season</option>
            {selectedPlayer.seasons.filter((season) => season.type == 'REG').map(s => {
            return (
            <option value={s.year} key={s.year}>{s.year}-{Number(s.year) + 1}</option>
          )
          })}
          </select></div>
        <table>
            <thead>
                <tr>
                    <th>Category:</th>
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
                    <td>{season.categories[2].ranks.find(rank => rank.player.id == player)? season.categories[2].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{season.categories[3].ranks.find(rank => rank.player.id == player)? season.categories[3].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{season.categories[0].ranks.find(rank => rank.player.id == player)? season.categories[0].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{season.categories[1].ranks.find(rank => rank.player.id == player)? season.categories[1].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{season.categories[5].ranks.find(rank => rank.player.id == player)? season.categories[5].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{season.categories[4].ranks.find(rank => rank.player.id == player)? season.categories[4].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{season.categories[6].ranks.find(rank => rank.player.id == player)? season.categories[6].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                    <td>{season.categories[7].ranks.find(rank => rank.player.id == player)? season.categories[7].ranks.find(rank => rank.player.id == player).rank: "N/R"}</td>
                </tr>
            </tbody>
        </table>
      </div>
      <div className="card">
        <div className="title">
          <h2>Posts</h2>
          {user &&
          <OpenModalButton
          modalComponent={<PostModal method={'POST'}/>}
          buttonText={'write a post'}
          onModalClose={(() => dispatch(getPlayerPosts(player)))} 
          />}
        </div>
        {posts &&
        <ul>{posts.map(post => {
          const created = new Date(post.created_at)
          return (
          <li key={post.id} className="posts">
            <h3>{post.title} {post.updated_at != post.created_at && "(edited)"}</h3>
            <p>By: {post.username}</p>
            <p>On: {created.toDateString()}</p>
            <p>{post.body}</p>
            <div id='post-buttons'>
              {user && user.id == post.user_id && 
                <OpenModalButton
                modalComponent={<PostModal method={'PUT'} postId={post.id}/>}
                buttonText={'edit'}
                onModalClose={(() => dispatch(getPlayerPosts(player)))} 
                />}
              {user && user.id == post.user_id && 
                <button className="btn" onClick={handleDelete(post.id)}>delete</button>}
            </div>
          </li>
        )})}
        </ul>}
        {!Object.keys(posts).length &&
        <p>No posts yet, be the first!</p>}
      </div> 
    </main>
  )
    } else return (
    <main>
      <h3 style={{alignSelf: 'center'}}>Player data not found</h3>
    </main>)
};

export default PlayerPage;
