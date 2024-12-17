import { useParams } from "react-router-dom";
import { seasonData } from "../../../data/season_data";
import { NavLink } from "react-router-dom";
//temporary year const, will change to select year
const year = 2023;

const CategoryPage = () => {
  const { category } = useParams()

  return (
    <div>
        <h1>{category.split('_').join(' ').toUpperCase()}</h1>
        <ol>
            {seasonData[year].categories.find(cat => cat.name == category).ranks.map(r => {
                const playerId = r.player.id
                return (
                    <li key={playerId}><NavLink to={`/players/${playerId}`}>{r.player.full_name}</NavLink></li>
                  )
            })}
        </ol>
    </div>
  )
};

export default CategoryPage;
