import React from "react";



const charCoin = (props) => {

    const {platinum, gold, silver, copper} = props;

    return(
        <div className="playerCoinGrid">
            <div className="border playerFlexRow">
                <h3>PP: {platinum}</h3>
                <h3>GP: {gold}</h3>
                <h3>SP: {silver}</h3> 
                <h3>CP: {copper}</h3>
            </div>
        </div>
    )
};

export default charCoin;