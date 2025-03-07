import { createBrowserRouter, Outlet } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import ProfilePage from '../components/ProfilePage';
import MainPage from '../components/MainPage';
import PlayerPage from '../components/PlayerPage';
import { playerData } from '../../data/player_data';
import Layout from './Layout';
import CategoryPage from '../components/CategoryPage';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <MainPage />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "current",
        element: <ProfilePage />,
      },
      {
        path: ":category",
        element: <CategoryPage />,
      },
      {
        path: "players",
        element: <Outlet />,
        children: [
          {
            path: "",
            element: <h3 style={{"textAlign": "center"}}>Use the dropdown above ⬆️ to select a player.</h3>
          },
          {
            path: ":playerId",
            element: <PlayerPage playerData={playerData}/>,
          }
        ]
      }
    ]
  }
]);