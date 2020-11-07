import React, {Component} from "react";

class charWeapon extends Component {

    state = {
        weapon_name: "Scimitar",
        damage : "1d8",
        dmg_type : "Slashing",
        critical: "x2"
    }

    render(){
        return(
            <div>
                <div className="border playerFlexRow">
                    <h4>{this.state.weapon_name}</h4>
                    <h4>{this.state.damage}/{this.state.critical}</h4>
                    <h4>{this.state.dmg_type}</h4>
                </div>
            </div>
        )
    };
    
}

export default charWeapon;