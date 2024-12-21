const SET_USER_POSTS = 'posts/setUserPosts'
const SET_PLAYER_POSTS = 'posts/setPlayerPosts'

export const setUserPosts = (posts) => ({
    type: SET_USER_POSTS,
    posts
  });

  export const setPlayerPosts = (posts) => ({
    type: SET_PLAYER_POSTS,
    posts
  });

export const getUserPosts = () => async (dispatch) => {
    const response = await fetch("/api/posts/current");
    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }
        console.log(data)
        dispatch(setUserPosts(data));
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
      default:
        return state;
    }
  }
  
  export default postReducer;