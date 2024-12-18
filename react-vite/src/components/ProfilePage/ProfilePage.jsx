import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
import UpdateAboutModal from "./UpdateAboutModal";

const ProfilePage = () => {
    const user = useSelector(state => state.session.user)
    const navigate = useNavigate()

    if (!user) navigate('/')

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
            <li>{user.top5?.one? user.top5.one: ""}</li>
            <li>{user.top5?.two? user.top5.two: ""}</li>
            <li>{user.top5?.three? user.top5.three: ""}</li>
            <li>{user.top5?.four? user.top5.four: ""}</li>
            <li>{user.top5?.five? user.top5.five: ""}</li> 
        </ol>
      </div>
      <div className="card">
        <h2>My Posts</h2>
      </div>
    </main>
  )
};

export default ProfilePage;
