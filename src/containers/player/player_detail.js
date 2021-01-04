import React, {useState} from "react";
import axios from "axios";
import CharImg from "../../components/player/char_img";
import CharMain from "../../components/player/char_main";
import CharAttr from "../../components/player/char_attr";
import CharHp from "../../components/player/char_hp";
import CharDeathSave from "../../components/player/char_deathsave";
import CharModifier from "../../components/player/char_modifier";
import CharSkill from "../../components/player/char_skill";
import CharAttack from "../../components/player/char_attack";
import CharFeat from "../../components/player/char_feat";
import CharEquip from "../../components/player/char_equip";
import CharCoin from "../../components/player/char_coin";
import Characteristics from "../../components/player/characteristics";
import CharNotes from "../../components/player/char_notes";

const PlayerDetail = props => {
    
    const [player, setPlayer] = useState(0);

        return(
            <div>
                <div className="playerDetailGrid">
                    <CharImg />
                    <CharMain playerId={player} />
                    <CharAttr playerId={player} />
                    <CharHp playerId={player} />
                    <CharDeathSave />
                    <CharModifier playerId={player}/>
                    <CharSkill playerId={player}/>
                    <CharAttack />
                    <CharFeat playerId={player} />
                    <CharEquip playerId={player} />
                    <CharCoin playerId={player} />
                    <Characteristics playerId={player} />
                    <CharNotes playerId={player} />
                </div>
            </div>
        )
}

export default PlayerDetail;
