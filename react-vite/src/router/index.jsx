import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import ProfilePage from '../components/ProfilePage';
import MainPage from '../components/MainPage';
import PlayerPage from '../components/PlayerPage';
import { playerData } from '../../data/player_data';
import Layout from './Layout';
import CategoryPage from '../components/CategoryPage';
//temporary year const, will change to select year
const year = 2023;

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
        path: "players/:playerId",
        element: <PlayerPage playerData={playerData} year={year}/>,
      },
    ],
  },
]);