import React from "react";

const charAc = (props) => {
    return(
        <div>
            <div className="border playerFlexRow">
                <h3>Regular: {props.ac.base}</h3>
                <h3>Flat-footed: {props.ac.base}+{props.ac.armor}</h3>
                <h3>Touch: 12</h3>
            </div>
        </div>
    )
};

export default charAc;