import { NavLink } from "react-router-dom";
import { seasonData } from "../../../data/season_data";
import { useState, useEffect } from "react";
import { setYear } from "../../redux/selected";
import { useDispatch, useSelector } from "react-redux";
import { getListThunk } from "../../redux/list";
import "./MainPage.css"

const MainPage = () => {

  const user = useSelector(state => state.session.user);
  const season = useSelector(state => state.selected.year);
  const [year, selectYear] = useState(season? season:2023);
  const dispatch = useDispatch();

    useEffect (() => {
      dispatch(setYear(year))
      if (user){
        dispatch(getListThunk())
      }
    })

  const handleChange = e => {
    selectYear(e.target.value)
    dispatch(setYear(e.target.value))
};
   
  return (
    <main>
      <h1>Welcome to NBA Rank</h1>
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
                        <li key={r.player.reference}><NavLink to={`players/${r.player.id}`}>{r.player.full_name}, {r.score > 1? r.score:(r.score*100).toFixed(1)}{r.score > 1? '/game':'%'}</NavLink></li>
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
