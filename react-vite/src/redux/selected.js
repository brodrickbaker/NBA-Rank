const SET_YEAR = 'selected/setYear';
const SET_PLAYER = 'selected/setPlayer';

export const setYear = (year) => ({
    type: SET_YEAR,
    payload: year
  });

export const setPlayer = (player) => ({
    type: SET_PLAYER,
    payload: player
  });


const initialState = { year: null, player: null };

function selectReducer(state = initialState, action) {
  switch (action.type) {
    case SET_YEAR:
      return { ...state, year: action.payload };
    case SET_PLAYER:
      return { ...state, player: action.payload };
    default:
      return state;
  }
}

export default selectReducer;