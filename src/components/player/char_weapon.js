import React from "react";

const CharWeapon = (props) => {

    const { name, dmg, dmgType, crit} = props;

        return(
            <div>
                <div className="border playerFlexRow">
                    <h4>{name}</h4>
                    <h4>{dmg}/{crit}</h4>
                    <h4>{dmgType}</h4>
                </div>
            </div>
        )
    };

export default CharWeapon;