import React, {Component} from "react";
import charImg from "../components/char_img";
import charMain from "../components/char_main";
import charAttr from "../components/char_attr";
import charHp from "../components/char_hp";
import charDeathSave from "../components/char_deathsave";
import charModifier from "../components/char_modifier";
import charSkill from "../components/char_skill";
import charAttack from "../components/char_attack";
import charFeat from "../components/char_feat";
import charEquip from "../components/char_equip";
import charCoin from "../components/char_coin";
import characteristics from "../components/characteristics";
import charNotes from "../components/char_notes";

class PlayerDetail extends Component {
    render() {
        return(
            <div>
                <div className="playerDetailGrid">
                    <charImg />
                    <charMain />
                    <charAttr />
                    <charHp />
                    <charDeathSave />
                    <charModifier />
                    <charSkill />
                    <charAttack />
                    <charFeat />
                    <charEquip />
                    <charCoin />
                    <characteristics />
                    <charNotes />
                </div>
            </div>
        )
    }
}

export default PlayerDetail;
