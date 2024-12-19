import { useSelector, useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
import UpdateAboutModal from "./UpdateAboutModal";
import { useEffect } from "react";
import { getListThunk } from "../../redux/list";
import { playerData } from "../../../data/player_data";

const ProfilePage = () => {
    const user = useSelector(state => state.session.user);
    const list = useSelector(state => state.list.list);
    const navigate = useNavigate();
    const dispatch = useDispatch();
    
    if (!user) navigate('/');

    useEffect(() => {
      dispatch(getListThunk())
    }, [dispatch])

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
            <li>{list.player_1? playerData[list.player_1].full_name: ""}</li>
            <li>{list.player_2? playerData[list.player_2].full_name: ""}</li>
            <li>{list.player_3? playerData[list.player_3].full_name: ""}</li>
            <li>{list.player_4? playerData[list.player_4].full_name: ""}</li>
            <li>{list.player_5? playerData[list.player_5].full_name: ""}</li> 
        </ol>
      </div>
      <div className="card">
        <h2>My Posts</h2>
      </div>
    </main>
  )
};

export default ProfilePage;
