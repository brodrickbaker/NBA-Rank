import { playerData } from "../../../data/player_data";
import { useNavigate } from "react-router-dom";
import { useContext, useState } from "react";
import { MyContext } from "../../router/Layout";
import { IoIosSearch } from "react-icons/io";

const PlayerSearch = () => {
 const {player, selectPlayer} = useContext(MyContext);
 const players = Object.keys(playerData);
 const [selectedPlayer, setSelectedPlayer] = useState(player) 

 players.sort((a, b) => {
    if (playerData[a].full_name < playerData[b].full_name) {
      return -1;
    }
    if (a.full_name > b.full_name) {
      return 1;
    }
    })

 const navigate = useNavigate();
 
 const handleChange = e => {
    setSelectedPlayer(e.target.value)
  };

 const handleSearch = e => {
    e.preventDefault()
    selectPlayer(selectedPlayer)
    navigate(`/players/${player}`)
 }

 return (
    <div id="player-search">
      <select name='player' id='player-select' onChange={handleChange} defaultValue='Select a player'>
        <option disabled>Select a player</option>
        {players.map(p =>{
            return (
                <option value={p} key={p}>{playerData[p].full_name}</option>
            )
        })}
      </select>
      <a onClick={handleSearch}><IoIosSearch  className="nav-item"/></a>  
    </div>
  )
};

export default PlayerSearch;
