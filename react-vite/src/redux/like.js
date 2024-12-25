const SET_LIKES = 'likes/setLikes';
const ADD_LIKE = 'likes/addLike';
const REMOVE_LIKE = 'likes/removeLike'
const CLEAR_LIKES = 'likes/clearLikes'

const setLikes = likes => ({
    type: SET_LIKES,
    likes
});

const addLike = like => ({
    type: ADD_LIKE,
    like
});

const removeLike = like => ({
    type: REMOVE_LIKE,
    like
})

export const clearLikes = () => ({
    type: CLEAR_LIKES
})



  
  export const getLikesThunk = (playerId) => async (dispatch) => {
    const response = await fetch(`/api/likes/${playerId}`);
    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            dispatch(clearLikes)
            return;
        }
        dispatch(setLikes(data));
    }
  };
  
  export const addLikeThunk = (playerId, userId) => async dispatch => {
  
    const response = await fetch(`/api/likes/${playerId}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({"player_id": playerId, "user_id": userId})
    });
  
    if(response.ok) {
        const data = await response.json();
        dispatch(addLike(data));
    } else if (response.status <= 400) {
      const errorMessages = await response.json();
      return errorMessages
    } else {
      return { server: "Something went wrong. Please try again" }
    }
  };

  export const removeLikeThunk = (playerId) => async dispatch => {

    const response = await fetch(`/api/likes/${playerId}`, {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
    });
  
    if(response.ok) {
        const data = await response.json();
        dispatch(removeLike(data));
    } else if (response.status <= 400) {
      const errorMessages = await response.json();
      return errorMessages
    } else {
      return { server: "Something went wrong. Please try again" }
    }
  }



const initialState = { playerLikes: {}};

function likeReducer(state = initialState, action) {
  switch (action.type) {
    case SET_LIKES: {
        const newState = {...state}
        newState.playerLikes = {}
        action.likes.forEach(like => {
            newState.playerLikes[like.user_id] = like
        });
        return newState;
        }
      case ADD_LIKE: {
        const newState = {...state}
        newState.playerLikes[action.like.user_id] = action.like
        return newState;
        }  
      case REMOVE_LIKE: {
        const newState = {...state}
        delete newState.playerLikes[action.like.user_id]
        return newState ; 
        }
      case CLEAR_LIKES:
        return { ...state, playerLikes: {} };
      default:  
        return state;
    }
}

export default likeReducer;