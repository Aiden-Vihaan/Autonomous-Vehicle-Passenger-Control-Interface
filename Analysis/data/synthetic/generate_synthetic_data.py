"""
EV-1.0 Synthetic Demonstration Dataset Generator

IMPORTANT:
This dataset is SYNTHETIC and NOT EMPIRICAL.

It exists only to demonstrate the analysis pipeline.
"""

from pathlib import Path
import numpy as np
import pandas as pd

SEED = 20260916
rng = np.random.default_rng(SEED)

N_PARTICIPANTS = 60
SCENARIOS_PER_PARTICIPANT = 6

conditions = ["A", "B", "C"]

scenario_definitions = [
    ("S01", "pedestrian", "medium"),
    ("S02", "emergency_vehicle", "high"),
    ("S03", "obstacle", "high"),
    ("S04", "lane_change", "medium"),
    ("S05", "intersection_pause", "low"),
    ("S06", "merging_vehicle", "medium"),
]

condition_effects = {
    "A": {
        "comprehension": 0.68,
        "trust": 3.35,
        "workload": 3.25,
        "understanding": 3.05,
        "response_time": 4600
    },
    "B": {
        "comprehension": 0.80,
        "trust": 3.70,
        "workload": 2.85,
        "understanding": 3.65,
        "response_time": 3900
    },
    "C": {
        "comprehension": 0.88,
        "trust": 4.05,
        "workload": 2.55,
        "understanding": 4.10,
        "response_time": 3300
    }
}

rows = []

for participant_number in range(1, N_PARTICIPANTS + 1):

    participant_id = f"P{participant_number:03d}"

    # Balanced demonstration assignment.
    participant_conditions = (
        conditions * 2
    )
    rng.shuffle(participant_conditions)

    for trial_number in range(SCENARIOS_PER_PARTICIPANT):

        scenario_id, event_type, urgency = scenario_definitions[trial_number]
        condition = participant_conditions[trial_number]

        effect = condition_effects[condition]

        comprehension_correct = int(
            rng.random() < effect["comprehension"]
        )

        response_time = max(
            1200,
            rng.normal(effect["response_time"], 750)
        )

        trust = int(
            np.clip(
                np.round(rng.normal(effect["trust"], 0.65)),
                1,
                5
            )
        )

        workload = int(
            np.clip(
                np.round(rng.normal(effect["workload"], 0.75)),
                1,
                5
            )
        )

        perceived_understanding = int(
            np.clip(
                np.round(rng.normal(effect["understanding"], 0.70)),
                1,
                5
            )
        )

        task_success = int(
            comprehension_correct == 1 and rng.random() > 0.05
        )

        interaction_error = int(
            rng.random() < (
                0.14 if condition == "A"
                else 0.09 if condition == "B"
                else 0.06
            )
        )

        rows.append({
            "participant_id": participant_id,
            "trial_id": f"{participant_id}_T{trial_number + 1:02d}",
            "scenario_id": scenario_id,
            "condition": condition,
            "event_type": event_type,
            "urgency": urgency,
            "explanation_timing": (
                "none" if condition == "A"
                else "during_event"
            ),
            "modality": "visual_text",
            "passenger_activity": "none",
            "comprehension_correct": comprehension_correct,
            "response_time_ms": round(response_time),
            "trust_score": trust,
            "workload_score": workload,
            "perceived_understanding": perceived_understanding,
            "task_success": task_success,
            "interaction_error": interaction_error,
            "technical_issue": 0,
            "protocol_deviation": 0,
            "missing_response": 0,
            "trial_interrupted": 0,
            "participant_withdrawal": 0,
            "invalid_trial": 0
        })

df = pd.DataFrame(rows)

output_path = Path(__file__).parent / "ev1_synthetic_trials.csv"
df.to_csv(output_path, index=False)

print("Synthetic dataset generated.")
print(f"Rows: {len(df)}")
print(f"Participants: {df['participant_id'].nunique()}")
print(f"Output: {output_path}")
print()
print("DATA STATUS: SYNTHETIC — NOT EMPIRICAL")
