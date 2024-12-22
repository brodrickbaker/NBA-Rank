const SET_USER_POSTS = 'posts/setUserPosts'
const SET_PLAYER_POSTS = 'posts/setPlayerPosts'
const CLEAR_PLAYER_POSTS = 'posts/clearPlayerPosts'
const UPDATE_POSTS = 'posts/updatePosts'
const REMOVE_POST = 'posts/removePost'

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

const updatePosts = (post) => ({
    type: UPDATE_POSTS,
    post
});

const removePost = (postId) => ({
    type: REMOVE_POST,
    postId
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
        if (data.errors) {
            dispatch(clearPlayerPosts());
            return;
        }
        dispatch(setPlayerPosts(data));
    }
  };

export const createPost = (postData, playerId) => async (dispatch) => {
    const response = await fetch(`/api/posts/${playerId}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            "title": postData.title,
            "body": postData.body
        })
      });
      if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return data;
        }
        dispatch(updatePosts(data));
    }
};

export const editPost = (postData, postId) => async (dispatch) => {
    const response = await fetch(`/api/posts/${postId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            "title": postData.title,
            "body": postData.body
        })
      });
      if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }
        dispatch(updatePosts(data));
    }
};

export const deletePost = (postId) => async (dispatch) => {
    const response = await fetch(`/api/posts/${postId}`, {
        method: "DELETE"
      });
      if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }
        dispatch(removePost(postId));
    }
};


const initialState = { 
    userPosts: null,
    playerPosts: {}
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
      case UPDATE_POSTS: {
        const newState = {...state}
        newState.playerPosts[action.post.id] = action.post
        return newState;
        }  
      case REMOVE_POST: {
        const newState = {...state}
        delete newState.playerPosts[action.postId]
        return newState ; 
        }
      case CLEAR_PLAYER_POSTS:
        return { ...state, playerPosts: {} };
      default:  
        return state;
    }
  }
  
  export default postReducer;