import React, {useState} from "react";
import CharWeapon from "./char_weapon";

const CharAttack = (weapons) => {

    return(
        <div className="playerAttackGrid playerFlexCol">
            <div className="border">
            {!weapons.length ? (
                <h1>No Weapons Found!</h1>
            ) : (
                weapons.map((weapon) => {
                    return (
                        <CharWeapon 
                            name={weapon.name}
                            dmg={weapon.dmg}
                            dmgType={weapon.dmgType}
                            crit={weapon.crit}
                            />
                    );
                })
            ) }
            </div>
        </div>
    )
};

export default CharAttack;