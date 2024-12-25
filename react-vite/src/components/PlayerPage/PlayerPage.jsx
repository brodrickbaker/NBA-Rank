import { useParams } from "react-router-dom";
import { seasonData } from "../../../data/season_data";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import { setPlayer } from "../../redux/selected";
import { addToList, getListThunk } from "../../redux/list";
import { getPlayerPosts, deletePost } from "../../redux/post";
import { getLikesThunk, addLikeThunk, removeLikeThunk, clearLikes } from "../../redux/like";
import OpenModalButton from "../OpenModalButton";
import PostModal from "./PostModal";

const PlayerPage = (props) => {
  const { playerData } = props;
  const { playerId } = useParams();  
  const player = playerData[playerId];
  const user = useSelector(state => state.session.user);
  const list = useSelector(state => state.list.list);
  let posts = useSelector(state => state.posts.playerPosts);
  let year = useSelector(state => state.selected.year);
  const playerLikes = useSelector(state => state.likes.playerLikes);
  const dispatch = useDispatch();

  const [isLoaded, setIsLoaded] = useState(false);
  const [likes, setLikes] = useState(playerLikes)

  if (!year) year = 2023

  useEffect (() => {
    dispatch(setPlayer(player.full_name))
    dispatch(getPlayerPosts(player.id))
    dispatch(clearLikes())
    dispatch(getListThunk())
    dispatch(getLikesThunk(player.id))
    setIsLoaded(true)
  }, [dispatch, player])
  
  const handleAdd = e => {
    e.preventDefault()
    dispatch(addToList(playerId))
  }

  const handleDelete = postId => e => {
    e.preventDefault()
    dispatch(deletePost(postId))
    .then(() => dispatch(getPlayerPosts(player.id)))
  }

  const handleLike = e => {
    e.preventDefault()
    console.log(likes)
    if(likes[user.id]) {
      dispatch(removeLikeThunk(player.id))
      setLikes(playerLikes)
    } else {
      dispatch(addLikeThunk(player.id))
      setLikes(playerLikes)
    }

  }

  if (isLoaded) {
    if (posts) posts = Object.values(posts)
    const stats = player.seasons.find(season => season.year == year).teams[0]

  return (
    <main>
      <h1>{player.full_name}</h1>
      <h2>{Object.values(likes).length} likes</h2>
      <button className='btn' onClick={handleLike}>Like</button>
      <h3>Position: {player.position}, Current Team: {player.team? player.team.name: 'Not Currently in NBA'}, Drafted: {player.draft.year} Rd {player.draft.round} Pk {player.draft.pick}, Years Pro: {player.seasons[0].year - player.draft.year + 1}</h3>
      {user && list && !Object.values(list).find(p => p == player.id) &&
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
        return (
          <li key={post.id}  className="card">
            <h3>{post.title} {post.updated_at != post.created_at && "(edited)"}</h3>
            <p>By: {post.username}</p>
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
