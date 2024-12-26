import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import PlayerSearch from "./PlayerSearch";
import "./Navigation.css";

function Navigation() {
  return (
    <ul className="nav">
      <li>
        <NavLink to="/">Home</NavLink>
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
