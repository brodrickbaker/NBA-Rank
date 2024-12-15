import { season2023 } from "../../../data/season_data";

const MainPage = () => {
  return (
    <main>
      <h1>Welcome to NBA Rank</h1>  
      <h2>Categories</h2>
      {season2023.categories.map(cat => {
        return (
        <div className="card" key={cat.name}>
            <h3>{cat.name.split('_').join(' ').toUpperCase()}</h3>
            <ol>
                {cat.ranks.map(r => {
                   if(r.rank <= 5){
                    return (
                        <li key={r.rank}>{r.player.full_name}, {r.score > 1? r.score:(r.score*100).toFixed(1)}{r.score > 1? '/game':'%'}</li>
                    )}
                })}
            </ol>
        </div>)
      })}
    </main>
  )
};

export default MainPage;
