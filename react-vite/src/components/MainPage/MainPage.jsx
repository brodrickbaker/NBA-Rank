import { useNavigate, NavLink } from "react-router-dom";
import { seasonData } from "../../../data/season_data";
import { useEffect, useContext } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getListThunk } from "../../redux/list";
import { MyContext } from "../../router/Layout";
import "./MainPage.css"

const MainPage = () => {

  const user = useSelector(state => state.session.user);
  const {year, selectYear, selectPlayer} = useContext(MyContext);
  const dispatch = useDispatch();
  const navigate = useNavigate();

    useEffect (() => {
      if (user){
        dispatch(getListThunk())
      }
    })

  const handleChange = e => {
    selectYear(e.target.value)
  };

  const handleClick = player => e =>{
    e.preventDefault()
    selectPlayer(player)
    navigate(`/players/${player}`)
  } 
   
  return (
    <main>
      <h1>Welcome to NBA Rank</h1>
      <h1>{year}-{Number(year) + 1} Season Leaders</h1>
      <label htmlFor='year-select'>Select a season</label>
      <select name='year' id='year-select' onChange={handleChange} defaultValue={year}>
        <option value={2023}>2023-2024</option>
        <option value={2022}>2022-2023</option>
        <option value={2021}>2021-2022</option>
        <option value={2020}>2020-2021</option>
        <option value={2019}>2019-2020</option>
      </select>  
      <h2>Categories</h2>
      <div className="categories"> 
      {seasonData[year].categories.map(cat => {
        return (
        <div className="card" key={cat.name}>
            <h3><NavLink to={cat.name}>{cat.name.split('_').join(' ').toUpperCase()}</NavLink></h3>
            <ol>
                {cat.ranks.map(r => {
                   if(r.rank <= 5){
                    return (
                        <li key={r.player.reference} onClick={handleClick(r.player.id)}>{r.player.full_name}, {r.score > 1? r.score:(r.score*100).toFixed(1)}{r.score > 1? '/game':'%'}</li>
                    )}
                })}
            </ol>
        </div>)
      })}
      </div>
    </main>
  )
};

export default MainPage;
