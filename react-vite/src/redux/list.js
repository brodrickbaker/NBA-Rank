const SET_LIST = 'selected/setList';

export const setList = (list) => ({
    type: SET_LIST,
    payload: list
  });

  
  export const getListThunk = () => async (dispatch) => {
    const response = await fetch("/api/lists/current");
    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }
        dispatch(setList(data));
    }
  };

  
  
  export const addToList = (player) => async dispatch => {
  
    const response = await fetch(`/api/lists/current`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({"player": player})
    });
  
    if(response.ok) {
        const data = await response.json();
        dispatch(setList(data));
    } else if (response.status <= 400) {
      const errorMessages = await response.json();
      return errorMessages
    } else {
      return { server: "Something went wrong. Please try again" }
    }
  };



const initialState = { list: null};

function listReducer(state = initialState, action) {
  switch (action.type) {
    case SET_LIST:
      return { ...state, list: action.payload };
    default:
      return state;
  }
}

export default listReducer;