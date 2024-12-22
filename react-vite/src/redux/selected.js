const SET_YEAR = 'selected/setYear';
const SET_PLAYER = 'selected/setPlayer';

export const setYear = (year) => ({
    type: SET_YEAR,
    year
  });

export const setPlayer = (player) => ({
    type: SET_PLAYER,
    player
  });


const initialState = { year: null, player: null };

function selectReducer(state = initialState, action) {
  switch (action.type) {
    case SET_YEAR:
      return { ...state, year: action.year };
    case SET_PLAYER:
      return { ...state, player: action.player };
    default:
      return state;
  }
}

export default selectReducer;