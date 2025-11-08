from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List
import json
import argparse

# ai.py
# GitHub Copilot
# Basic heuristic assistant to evaluate when a Magic: The Gathering card is best used.


# Simple card model (add fields as needed)
@dataclass
class Card:
    name: str
    mana_cost: int = 0
    card_type: str = "instant"  # instant, sorcery, creature, enchantment, artifact, planeswalker
    effect: str = ""  # free text description
    damage: int = 0  # direct damage to player
    creature_damage: int = 0  # damage to creature(s)
    heal: int = 0
    draw: int = 0
    buff_power: int = 0
    buff_toughness: int = 0
    remove_creature: bool = False
    board_wipe: bool = False
    counter: bool = False
    speed: str = "instant"  # instant or sorcery-like timing
    tags: List[str] = field(default_factory=list)

@dataclass
class GameState:
    turn: int = 1
    my_life: int = 20
    opp_life: int = 20
    my_board: int = 0  # count of creatures
    opp_board: int = 0
    my_hand: int = 0
    opp_hand: int = 0
    my_total_power: int = 0
    opp_total_power: int = 0
    imminent_opp_lethal: bool = False
    important_opp_permanent_present: bool = False  # e.g., big threat, planeswalker
    tempo_deficit: int = 0  # positive means behind on board/pressure

def score_card_for_state(card: Card, s: GameState) -> Dict[str, Any]:
    # Heuristic scoring for early/mid/late and immediate use
    scores = {"early": 0.0, "mid": 0.0, "late": 0.0, "immediate": 0.0}
    reasons: List[str] = []

    # Base preferences by card type and speed
    if card.speed == "instant":
        scores["immediate"] += 0.6
    if card.card_type == "creature":
        scores["early"] += 0.5
        scores["mid"] += 0.3
    if card.card_type in ("sorcery", "enchantment", "planeswalker", "artifact"):
        scores["mid"] += 0.4
        scores["late"] += 0.4

    # Direct damage: prefer when opponent low or to finish
    if card.damage > 0:
        if s.opp_life <= card.damage + 2:
            scores["immediate"] += 1.0
            reasons.append("Can potentially finish opponent")
        else:
            scores["mid"] += 0.3
            scores["late"] += 0.2
            reasons.append("Damage useful as reach later")

    # Creature removal: best when opponent has a threatening creature
    if card.remove_creature or card.creature_damage > 0:
        # prefer immediate if opponent has threats or imminent lethal
        if s.imminent_opp_lethal or s.opp_total_power > s.my_total_power + 3 or s.important_opp_permanent_present:
            scores["immediate"] += 1.0
            reasons.append("Removal needed to stop lethal/major threat")
        elif s.opp_board >= 3:
            scores["mid"] += 0.8
            reasons.append("Good to stop wide boards in midgame")
        else:
            scores["early"] += 0.4
            reasons.append("Early tempo advantage")

    # Board wipe preference
    if card.board_wipe:
        if s.opp_board - s.my_board >= 2:
            scores["immediate"] += 1.2
            reasons.append("Clear opponent's wide board advantage now")
        else:
            scores["mid"] += 0.6
            reasons.append("Better used in midgame when boards are developed")

    # Card draw
    if card.draw > 0:
        if s.my_hand <= 1:
            scores["immediate"] += 0.8
            reasons.append("Low hand size -> draw now")
        else:
            scores["mid"] += 0.5
            reasons.append("Card advantage useful in midgame")

    # Heal / life gain
    if card.heal > 0:
        if s.my_life <= 6:
            scores["immediate"] += 1.0
            reasons.append("Heal needed to survive")
        else:
            scores["late"] += 0.4
            reasons.append("Life buffer for late game")

    # Buffs
    if card.buff_power or card.buff_toughness:
        if s.my_board > 0:
            # prefer attacking (mid) or immediate if lethal push possible
            if s.opp_life <= s.my_total_power + card.buff_power * s.my_board:
                scores["immediate"] += 0.9
                reasons.append("Buff enables lethal attack")
            else:
                scores["mid"] += 0.7
                reasons.append("Buff helpful in combat / midgame")
        else:
            scores["early"] += 0.2
            reasons.append("No creatures to buff yet")

    # Counterspells
    if card.counter:
        if s.important_opp_permanent_present or s.imminent_opp_lethal:
            scores["immediate"] += 1.2
            reasons.append("Counter important spell now")
        else:
            scores["mid"] += 0.4
            reasons.append("Keep for high-value opponent spells")

    # Tempo consideration: when behind prefer removal/board wipe now, creatures early
    if s.tempo_deficit > 1:
        scores["immediate"] += 0.7
        reasons.append("Behind on tempo -> play impactful answers now")
    elif s.tempo_deficit < -1:
        scores["early"] += 0.5
        reasons.append("Ahead on tempo -> develop threats early")

    # Normalize and pick
    # small smoothing to allow comparisons
    for k in scores:
        scores[k] = float(scores[k])

    # Choose best slot
    best_slot = max(scores, key=scores.get)
    explanation = "; ".join(reasons) if reasons else "No strong heuristics; choose flexibility."
    return {"card": card.name, "best": best_slot, "scores": scores, "explanation": explanation}

def parse_card_from_json(text: str) -> Card:
    data = json.loads(text)
    return Card(
        name=data.get("name", "Unknown"),
        mana_cost=int(data.get("mana_cost", 0)),
        card_type=data.get("card_type", "instant"),
        effect=data.get("effect", ""),
        damage=int(data.get("damage", 0)),
        creature_damage=int(data.get("creature_damage", 0)),
        heal=int(data.get("heal", 0)),
        draw=int(data.get("draw", 0)),
        buff_power=int(data.get("buff_power", 0)),
        buff_toughness=int(data.get("buff_toughness", 0)),
        remove_creature=bool(data.get("remove_creature", False)),
        board_wipe=bool(data.get("board_wipe", False)),
        counter=bool(data.get("counter", False)),
        speed=data.get("speed", "instant"),
        tags=data.get("tags", []),
    )

def parse_state_from_json(text: str) -> GameState:
    data = json.loads(text)
    return GameState(
        turn=int(data.get("turn", 1)),
        my_life=int(data.get("my_life", 20)),
        opp_life=int(data.get("opp_life", 20)),
        my_board=int(data.get("my_board", 0)),
        opp_board=int(data.get("opp_board", 0)),
        my_hand=int(data.get("my_hand", 0)),
        opp_hand=int(data.get("opp_hand", 0)),
        my_total_power=int(data.get("my_total_power", 0)),
        opp_total_power=int(data.get("opp_total_power", 0)),
        imminent_opp_lethal=bool(data.get("imminent_opp_lethal", False)),
        important_opp_permanent_present=bool(data.get("important_opp_permanent_present", False)),
        tempo_deficit=int(data.get("tempo_deficit", 0)),
    )

def demo():
    # Example usage
    sample_card = Card(
        name="Fireblast",
        mana_cost=2,
        card_type="instant",
        damage=4,
        effect="Deal 4 damage to any target",
        speed="instant"
    )
    state = GameState(turn=6, my_life=10, opp_life=5, my_board=1, opp_board=2,
                      my_hand=2, opp_hand=1, my_total_power=3, opp_total_power=6,
                      imminent_opp_lethal=False, important_opp_permanent_present=False, tempo_deficit=1)
    result = score_card_for_state(sample_card, state)
    print("Sample card evaluation:", json.dumps(result, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple MTG timing advisor")
    parser.add_argument("--card", help="Card JSON (or path to .json file). If omitted, demo runs.")
    parser.add_argument("--state", help="Game state JSON (or path).")
    args = parser.parse_args()

    if not args.card:
        demo()
    else:
        # load card json
        text_card = args.card
        try:
            with open(text_card, "r") as f:
                text_card = f.read()
        except Exception:
            pass
        card = parse_card_from_json(text_card)

        if args.state:
            text_state = args.state
            try:
                with open(text_state, "r") as f:
                    text_state = f.read()
            except Exception:
                pass
            state = parse_state_from_json(text_state)
        else:
            # simple interactive state inputs
            print("No state provided. Using quick interactive prompts.")
            state = GameState()
            try:
                state.turn = int(input("Turn number (default 1): ") or 1)
                state.my_life = int(input("Your life (default 20): ") or 20)
                state.opp_life = int(input("Opp life (default 20): ") or 20)
                state.my_board = int(input("Your creatures on board: ") or 0)
                state.opp_board = int(input("Opp creatures on board: ") or 0)
                state.my_hand = int(input("Your hand size: ") or 0)
                state.opp_hand = int(input("Opp hand size: ") or 0)
                state.my_total_power = int(input("Your total power on board: ") or 0)
                state.opp_total_power = int(input("Opp total power on board: ") or 0)
                state.imminent_opp_lethal = (input("Imminent opponent lethal? (y/N): ").lower() == "y")
                state.important_opp_permanent_present = (input("Important opponent permanent present? (y/N): ").lower() == "y")
                state.tempo_deficit = int(input("Tempo deficit (pos = you're behind): ") or 0)
            except Exception:
                print("Invalid input, using defaults.")

        res = score_card_for_state(card, state)
        print(json.dumps(res, indent=2))