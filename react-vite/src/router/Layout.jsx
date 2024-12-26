import { useEffect, useState, createContext } from "react";
import { Outlet } from "react-router-dom";
import { useDispatch } from "react-redux";
import { ModalProvider, Modal } from "../context/Modal";
import { thunkAuthenticate } from "../redux/session";
import Navigation from "../components/Navigation/Navigation";

export const MyContext = createContext();

export default function Layout() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  const [player, selectPlayer] = useState('')
  const [year, selectYear] = useState(2023)

  useEffect(() => {
    dispatch(thunkAuthenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <ModalProvider>
        <MyContext.Provider value={{player, selectPlayer, year, selectYear}}>
        <Navigation />
        {isLoaded && <Outlet />}
        <Modal />
        </MyContext.Provider>
      </ModalProvider>
    </>
  );
}
