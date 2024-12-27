import { useSelector, useDispatch } from "react-redux";
import { useState } from "react";
import { createPost, editPost, getPlayerPosts} from "../../redux/post";
import { useModal } from "../../context/Modal";
import { useParams } from "react-router-dom";

const PostModal = (props) => {
    const { method, postId } = props;
    const posts = useSelector(state => state.posts.playerPosts);
    const [title, setTitle] = useState(postId? posts[postId].title:'');
    const [body, setBody] = useState(postId? posts[postId].body:'');
    
    const { playerId } = useParams();
    const dispatch = useDispatch();
    const {closeModal} = useModal();

    const writePost = async (e) => {
        e.preventDefault();
        const post = {title: title, body: body}
        if(method == 'POST') {
            dispatch(createPost(post, playerId))
            .then(() => dispatch(getPlayerPosts(playerId)))
        }
        if(method == 'PUT') {
            console.log(post)
            dispatch(editPost(post, postId))
            .then(() => dispatch(getPlayerPosts(playerId)))
        } 
        closeModal()
    }

    return (
    <div>
        <form onSubmit={writePost}>
        <h2>Write a Post</h2>
        <input
            type="text"
            placeholder="Post Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        <textarea
            name='body'
            placeholder="What makes him great?"
            value={body}
            rows='5'
            cols='50'
            onChange={(e) => setBody(e.target.value)}>
        </textarea>
            <button className="btn" type="submit">Post</button>
        </form>
    </div>
  )
};

export default PostModal;