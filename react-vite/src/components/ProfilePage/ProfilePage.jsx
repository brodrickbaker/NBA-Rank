import { useSelector, useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
import UpdateAboutModal from "./UpdateAboutModal";
import { useEffect, useState } from "react";
import { getListThunk, deletePlayer } from "../../redux/list";
import { playerData } from "../../../data/player_data";
import { NavLink } from "react-router-dom";
import { getUserPosts } from "../../redux/post";

const ProfilePage = () => {
    const user = useSelector(state => state.session.user);
    const list = useSelector(state => state.list.list);
    let posts = useSelector(state => state.posts.userPosts);
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const [isLoaded, setIsLoaded] = useState(false);
    
    if (!user) navigate('/');

    useEffect(() => {
      dispatch(getListThunk())
      .then(() => dispatch(getUserPosts())
      .then(() => setIsLoaded(true)))
    }, [dispatch])

    const handleDelete = playerId => e => {
      e.preventDefault()
      dispatch(deletePlayer(playerId))
    }

    if(isLoaded){
      if (posts) posts = Object.values(posts)

    return (
    <main>
      <h1>{user.username}</h1>
      <div id="about" className="card">
        <h2>About Me</h2>
        <p>{user.about? user.about:"Say a little something about yourself"}</p>
        <OpenModalButton
          modalComponent={<UpdateAboutModal/>}
          buttonText={'edit'} 
        />
      </div>
      <div id="top5" className="card">
        <h2>My Top 5</h2>
        <ol>
            <li>{list.player_1? <NavLink to={`/players/${list.player_1}`}>{playerData[list.player_1].full_name}</NavLink>: ""} {list.player_1 && <button className="btn" onClick={handleDelete(list.player_1)}>Delete</button>}</li>
            <li>{list.player_2? <NavLink to={`/players/${list.player_2}`}>{playerData[list.player_2].full_name}</NavLink>: ""} {list.player_2 && <button className="btn" onClick={handleDelete(list.player_2)}>Delete</button>}</li>
            <li>{list.player_3? <NavLink to={`/players/${list.player_3}`}>{playerData[list.player_3].full_name}</NavLink>: ""} {list.player_3 && <button className="btn" onClick={handleDelete(list.player_3)}>Delete</button>}</li>
            <li>{list.player_4? <NavLink to={`/players/${list.player_4}`}>{playerData[list.player_4].full_name}</NavLink>: ""} {list.player_4 && <button className="btn" onClick={handleDelete(list.player_4)}>Delete</button>}</li>
            <li>{list.player_5? <NavLink to={`/players/${list.player_5}`}>{playerData[list.player_5].full_name}</NavLink>: ""} {list.player_5 && <button className="btn" onClick={handleDelete(list.player_5)}>Delete</button>}</li> 
        </ol>
      </div>
      <div className="card">
        <h2>My Posts</h2>
        {posts &&
        <ul>{posts.map(post => {
          return (
            <li key={post.id}  className="card">
              <h3>{post.title} {post.updated_at != post.created_at? "(edited)":""}</h3>
              <p>About:<NavLink to={`/players/${post.player_id}`}> {playerData[post.player_id].full_name}</NavLink></p>
              <p>{post.body}</p>
            </li>
          )})}
          </ul>}
          {!posts &&
          <p>No posts yet</p>}
      </div>
    </main>
  )}
};

export default ProfilePage;
