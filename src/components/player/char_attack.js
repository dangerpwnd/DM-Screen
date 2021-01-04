import React, {useState} from "react";
import CharWeapon from "./char_weapon";

const CharAttack = props => {

    const player = props.playerId;

    const [weapon, setWeapon] = useState({
        weapon_name: "Scimitar",
        damage : "1d8",
        dmg_type : "Slashing",
        critical: "x2"
    })

    return(
        <div className="playerAttackGrid playerFlexCol">
            <div className="border">
                <CharWeapon weapon={weapon} />
                <CharWeapon weapon={weapon} />
                <CharWeapon weapon={weapon} />
            </div>
        </div>
    )
};

export default CharAttack;