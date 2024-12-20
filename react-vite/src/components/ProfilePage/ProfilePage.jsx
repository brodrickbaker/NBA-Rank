import { useSelector, useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
import UpdateAboutModal from "./UpdateAboutModal";
import { useEffect } from "react";
import { getListThunk, deletePlayer } from "../../redux/list";
import { playerData } from "../../../data/player_data";
import { NavLink } from "react-router-dom";

const ProfilePage = () => {
    const user = useSelector(state => state.session.user);
    const list = useSelector(state => state.list.list);
    const navigate = useNavigate();
    const dispatch = useDispatch();
    
    if (!user) navigate('/');

    useEffect(() => {
      dispatch(getListThunk())
    }, [dispatch])

    const handleDelete = playerId => e => {
      e.preventDefault()
      dispatch(deletePlayer(playerId))
    }

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
      </div>
    </main>
  )
};

export default ProfilePage;
