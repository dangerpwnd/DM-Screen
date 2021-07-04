import React from "react";

const charHp = (props) => {

    const { current, maxHP, hitDice} = props

    return(
        <div className="playerHpGrid">
            <div className="border playerFlexRow">
                <h3>Current: {current}</h3>
                <h3>Max: {maxHP}</h3>
                <h3>Hit Dice: {hitDice}</h3> 
            </div>
            
        </div>
    )
};

export default charHp;