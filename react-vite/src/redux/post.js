const SET_USER_POSTS = 'posts/setUserPosts'
const SET_PLAYER_POSTS = 'posts/setPlayerPosts'
const CLEAR_PLAYER_POSTS = 'posts/clearPlayerPosts'

const setUserPosts = (posts) => ({
    type: SET_USER_POSTS,
    posts
  });

const setPlayerPosts = (posts) => ({
    type: SET_PLAYER_POSTS,
    posts
  });

const clearPlayerPosts = () => ({
    type: CLEAR_PLAYER_POSTS,
    posts: null
});

export const getUserPosts = () => async (dispatch) => {
    const response = await fetch("/api/posts/current");
    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }
        dispatch(setUserPosts(data));
    }
  };

export const getPlayerPosts = (playerId) => async (dispatch) => {
    const response = await fetch(`/api/posts/${playerId}`);
    if (response.ok) {
        const data = await response.json();
        console.log(data)
        if (data.errors) {
            dispatch(clearPlayerPosts());
            return;
        }
        dispatch(setPlayerPosts(data));
    }
  };


const initialState = { 
    userPosts: null,
    playerPosts: null
};

function postReducer(state = initialState, action) {
    switch (action.type) {
      case SET_USER_POSTS: {
        const newState = {...state}
        newState.userPosts = {}
        action.posts.forEach(post => {
            newState.userPosts[post.id] = post
        });
        return newState;
        }
      case SET_PLAYER_POSTS: {
        const newState = {...state}
        newState.playerPosts = {}
        action.posts.forEach(post => {
            newState.playerPosts[post.id] = post
        });
        return newState;
        }
      case CLEAR_PLAYER_POSTS:
        return { ...state, playerPosts: null };  
      default:
        return state;
    }
  }
  
  export default postReducer;