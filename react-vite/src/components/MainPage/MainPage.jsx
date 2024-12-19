import { NavLink } from "react-router-dom";
import { seasonData } from "../../../data/season_data";
import { useState, useEffect } from "react";
import { setYear } from "../../redux/selected";
import { useDispatch } from "react-redux";
import { getListThunk } from "../../redux/list";
import "./MainPage.css"

const MainPage = () => {
  const [year, selectYear] = useState(2023)
  const dispatch = useDispatch()

    useEffect (() => {
      dispatch(setYear(year))
      dispatch(getListThunk())
    })

  const handleChange = e => {
    selectYear(e.target.value)
    dispatch(setYear(e.target.value))
};
   
  return (
    <main>
      <h1>Welcome to NBA Rank</h1>
      <label htmlFor='year-select'>Select a year</label>
      <select name='year' id='year-select' onChange={handleChange}>
        <option value={2023}>2023</option>
        <option value={2022}>2022</option>
        <option value={2021}>2021</option>
        <option value={2020}>2020</option>
        <option value={2019}>2019</option>
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
