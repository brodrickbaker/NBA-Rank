import { useSelector, useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
import UpdateAboutModal from "./UpdateAboutModal";
import { useEffect, useState } from "react";
import { getListThunk, deletePlayer } from "../../redux/list";
import { playerData } from "../../../data/player_data";
import { getUserPosts } from "../../redux/post";
import { useContext } from "react";
import { MyContext } from "../../router/Layout";


const ProfilePage = () => {
    const user = useSelector(state => state.session.user);
    const list = useSelector(state => state.list.list);
    let posts = useSelector(state => state.posts.userPosts);
    const { selectPlayer } = useContext(MyContext);
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

    const handleClick = player => e =>{
      e.preventDefault()
      selectPlayer(player)
      navigate(`/players/${player}`)
    } 

    if(isLoaded){
      if (posts) posts = Object.values(posts)

    return (
    <main>
      <h1>{user.username}</h1>
      <div id="user-data">
      <div id="about" className="card">
        <div className="title">
          <h2>About Me</h2>
          <OpenModalButton
          modalComponent={<UpdateAboutModal/>}
          buttonText={'edit'} 
          />
        </div>
        <p>{user.about? user.about:"Say a little something about yourself"}</p>
      </div>
      <div id="top-5" className="card">
        <h2>My Top 5</h2>
        <ol>
            <li>{list.player_1? <a onClick={handleClick(list.player_1)}>{playerData[list.player_1].full_name}</a>: ""} {list.player_1 && <button className="btn" onClick={handleDelete(list.player_1)}>Delete</button>}</li>
            <li>{list.player_2? <a onClick={handleClick(list.player_2)}>{playerData[list.player_2].full_name}</a>: ""} {list.player_2 && <button className="btn" onClick={handleDelete(list.player_2)}>Delete</button>}</li>
            <li>{list.player_3? <a onClick={handleClick(list.player_3)}>{playerData[list.player_3].full_name}</a>: ""} {list.player_3 && <button className="btn" onClick={handleDelete(list.player_3)}>Delete</button>}</li>
            <li>{list.player_4? <a onClick={handleClick(list.player_4)}>{playerData[list.player_4].full_name}</a>: ""} {list.player_4 && <button className="btn" onClick={handleDelete(list.player_4)}>Delete</button>}</li>
            <li>{list.player_5? <a onClick={handleClick(list.player_5)}>{playerData[list.player_5].full_name}</a>: ""} {list.player_5 && <button className="btn" onClick={handleDelete(list.player_5)}>Delete</button>}</li> 
        </ol>
      </div>
      </div>
      <div className="card">
        <h2>My Posts</h2>
        {posts &&
        <ul>{posts.map(post => {
          return (
            <li key={post.id} className="posts">
              <h3>{post.title} {post.updated_at != post.created_at? "(edited)":""}</h3>
              <p>About:<a onClick={handleClick(post.player_id)}> {playerData[post.player_id].full_name}</a></p>
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
