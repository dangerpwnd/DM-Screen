import React, {Component} from "react";
import CharImg from "../components/char_img";
import CharMain from "../components/char_main";
import CharAttr from "../components/char_attr";
import CharHp from "../components/char_hp";
import CharDeathSave from "../components/char_deathsave";
import CharModifier from "../components/char_modifier";
import CharSkill from "../components/char_skill";
import CharAttack from "../components/char_attack";
import CharFeat from "../components/char_feat";
import CharEquip from "../components/char_equip";
import CharCoin from "../components/char_coin";
import Characteristics from "../components/characteristics";
import CharNotes from "../components/char_notes";

class PlayerDetail extends Component {

    state = {
        ac: {
            base: 10,
            nat: 0,
            dex: 2,
            armor: 2,
            magic: 1
        },
        attr: {
            str: 10,
            dex: 10,
            con: 10,
            int: 10,
            wis: 10,
            cha: 10
        },
        hp: {
            current: 1,
            max: 1,
            hdice: 1
        },
        level: {
            current: 1
        },
        attr_mod: {
            str: 0,
            dex: 0,
            con: 0,
            int: 0,
            wis: 0,
            char: 0
        },
        skill: {
            acrobatics: 0,
            animal: 0,
            arcana: 0,
            athletics: 0,
            deception: 0,
            history: 0,
            insight: 0,
            intimidation: 0,
            investigation: 0,
            medicine: 0,
            nature: 0,
            perception: 0,
            performance: 0,
            persuasion: 0,
            religion: 0,
            sleight: 0,
            stealth: 0,
            survival: 0
        }
    }

    render() {
        return(
            <div>
                <div className="playerDetailGrid">
                    <CharImg />
                    <CharMain ac={this.state.ac}/>
                    <CharAttr attr={this.state.attr}/>
                    <CharHp hp={this.state.hp}/>
                    <CharDeathSave />
                    <CharModifier attr_mod={this.state.attr_mod}/>
                    <CharSkill skill={this.state.skill}/>
                    <CharAttack />
                    <CharFeat />
                    <CharEquip />
                    <CharCoin />
                    <Characteristics />
                    <CharNotes />
                </div>
            </div>
        )
    }
}

export default PlayerDetail;
