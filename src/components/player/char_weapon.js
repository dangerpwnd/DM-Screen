import React from "react";

const CharWeapon = (props) => {

        return(
            <div>
                <div className="border playerFlexRow">
                    <h4>{props.weapon.weapon_name}</h4>
                    <h4>{props.weapon.damage}/{props.weapon.critical}</h4>
                    <h4>{props.weapon.dmg_type}</h4>
                </div>
            </div>
        )
    };

export default CharWeapon;