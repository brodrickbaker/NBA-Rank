import { useSelector, useDispatch } from "react-redux";
import { useState } from "react";
import { thunkAbout } from "../../redux/session";
import { useModal } from "../../context/Modal";

const UpdateAboutModal = () => {
    const user = useSelector(state => state.session.user)
    const [about, setAbout] = useState(user.about? user.about:"Say a little something about yourself")
    const dispatch = useDispatch()
    const {closeModal} = useModal()

    const updateAbout = async (e) => {
        e.preventDefault();
        dispatch(thunkAbout(about, user.id))
        closeModal()
    }

    return (
    <div className="card">
        <form onSubmit={updateAbout}>
        <input
            type="text"
            value={about}
            onChange={(e) => setAbout(e.target.value)}
            required
          />
           {/* <textarea
                name='about'
                value={about}
                rows='5'
                onChange={setAbout} >
            </textarea> */}
            <button className="btn" type="submit">Update</button>
        </form>
    </div>
  )
};

export default UpdateAboutModal;
