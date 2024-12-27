import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import PlayerSearch from "./PlayerSearch";
import { MdOutlineSportsBasketball } from "react-icons/md";
import "./Navigation.css";

function Navigation() {
  return (
    <ul className="nav">
      <li>
        <NavLink to="/"><MdOutlineSportsBasketball className='nav-item'/>
        </NavLink>
      </li>
      <li>
        <PlayerSearch />
      </li>
      <li>
        <ProfileButton />
      </li>
    </ul>
  );
}

export default Navigation;
