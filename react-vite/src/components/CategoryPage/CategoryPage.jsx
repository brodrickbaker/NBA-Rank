import { useParams } from "react-router-dom";
import { seasonData } from "../../../data/season_data";
import { useNavigate } from "react-router-dom";
import { useContext } from "react";
import { MyContext } from "../../router/Layout";

const CategoryPage = () => {
  
  const {year, selectPlayer} = useContext(MyContext);
  const { category } = useParams();
  const navigate = useNavigate();

  
  const handleClick = player => e =>{
    e.preventDefault()
    selectPlayer(player)
    navigate(`/players/${player}`)
  } 

  return (
    <main>
        <h1>{year}-{Number(year) + 1} {category.split('_').join(' ').toUpperCase()} LEADERS</h1>
        <ol id='category-page'>
            {seasonData[year].categories.find(cat => cat.name == category).ranks?.map(r => {
                const playerId = r.player.id
                return (
                    <li key={playerId}><a onClick={handleClick(playerId)}>{r.player.full_name}</a></li>
                  )
            })}
        </ol>
    </main>
  )
};

export default CategoryPage;
