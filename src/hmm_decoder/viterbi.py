"""
PathSnap: Hidden Markov Model (HMM) & Viterbi Route Reconstruction.
Owned by Member 3 (You: HMM/Viterbi).

Key outputs:
- decode_trip(trip_id, ...) -> List[int] of arc IDs
- Classifier-only vs HMM comparison
- Report Sections 5 & 6
"""

from typing import List, Tuple
import logging

logger = logging.getLogger("pathsnap.hmm")

def decode_trip(
    trip_id: str,
    gps_coords: List[List[float]],
    nodes: List[List[float]],
    arcs: List[Tuple[int, int]]
) -> List[int]:
    """
    Reconstructs the optimal sequence of road segments (arc IDs) from noisy GPS.
    
    HMM Formulation:
    - Hidden States: Candidate road segments (arcs) near each GPS observation
    - Emission Probabilities: Based on spatial distance (e.g. Gaussian distribution or classifier probability)
    - Transition Probabilities: Based on shortest network path distance vs great circle distance between consecutive GPS points
    - Decoding: Viterbi dynamic programming algorithm with gap/disconnection penalty
    """
    # Member 3 will complete this implementation.
    # Currently raising NotImplementedError so inference.py falls back cleanly during testing.
    raise NotImplementedError("Member 3 is currently tuning the Viterbi decoder.")
