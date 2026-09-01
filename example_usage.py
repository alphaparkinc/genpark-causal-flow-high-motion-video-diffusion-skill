from client import CausalFlowHighMotionVideoDiffusionClient

def main():
    client = CausalFlowHighMotionVideoDiffusionClient()
    res = client.sample_high_motion_video('High-speed racing car navigating mountain switchbacks in heavy rain', 4)
    print('Wan Video Diffusion: ' + res['diffusion_job_id'] + ' (' + str(res['temporal_frames_count']) + ' frames)')
    print('Causal Flow Consistency: ' + str(res['causal_flow_consistency_score']) + ' | Smoothness: ' + str(res['optical_flow_motion_smoothness_pct']) + '%')
    print('Video Output: ' + res['rendered_mp4_video_url'])

if __name__ == '__main__':
    main()
