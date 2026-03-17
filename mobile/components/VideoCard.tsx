import React, { useState, useEffect, useRef } from 'react';
import { View, Text, StyleSheet, Dimensions, TouchableOpacity } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Video, ResizeMode, AVPlaybackStatus } from 'expo-av';
import { VideoWithCareer, recordEngagement } from '../services/api';

const { height, width } = Dimensions.get('window');

interface VideoCardProps {
  video: VideoWithCareer;
  isActive: boolean;
}

export default function VideoCard({ video, isActive }: VideoCardProps) {
  const [liked, setLiked] = useState(false);
  const [saved, setSaved] = useState(false);
  const [watchStartTime, setWatchStartTime] = useState<number | null>(null);
  const videoRef = useRef<Video>(null);

  useEffect(() => {
    if (isActive) {
      videoRef.current?.playAsync();
      setWatchStartTime(Date.now());
    } else {
      videoRef.current?.pauseAsync();
      if (watchStartTime) {
        const watchDuration = (Date.now() - watchStartTime) / 1000;
        recordEngagement({
          career_id: video.career_id,
          video_id: video.id,
          action: 'watched',
          watch_duration_seconds: watchDuration,
        });
      }
      setWatchStartTime(null);
    }
  }, [isActive]);

  const handleLike = async () => {
    const newLiked = !liked;
    setLiked(newLiked);
    if (newLiked) {
      await recordEngagement({
        career_id: video.career_id,
        video_id: video.id,
        action: 'liked',
      });
    }
  };

  const handleSave = async () => {
    const newSaved = !saved;
    setSaved(newSaved);
    if (newSaved) {
      await recordEngagement({
        career_id: video.career_id,
        video_id: video.id,
        action: 'saved',
      });
    }
  };

  const handleShare = async () => {
    await recordEngagement({
      career_id: video.career_id,
      video_id: video.id,
      action: 'shared',
    });
    // TODO: Implement native share functionality
  };

  const handleSkip = async () => {
    await recordEngagement({
      career_id: video.career_id,
      video_id: video.id,
      action: 'skipped',
    });
    // TODO: Scroll to next video
  };

  const formatSalary = () => {
    const { salary_range_min, salary_range_max } = video.career;
    if (salary_range_min && salary_range_max) {
      return `$${(salary_range_min / 1000).toFixed(0)}K-$${(salary_range_max / 1000).toFixed(0)}K/year`;
    } else if (salary_range_min) {
      return `$${(salary_range_min / 1000).toFixed(0)}K+/year`;
    }
    return 'Salary varies';
  };

  return (
    <View style={styles.container}>
      {/* Video player */}
      <Video
        ref={videoRef}
        source={{ uri: video.blob_url }}
        style={styles.video}
        resizeMode={ResizeMode.COVER}
        isLooping
        shouldPlay={isActive}
        useNativeControls={false}
      />

      {/* Gradient overlay */}
      <LinearGradient
        colors={['transparent', 'rgba(0,0,0,0.8)']}
        style={styles.gradient}
      />

      {/* Career info */}
      <View style={styles.infoContainer}>
        <Text style={styles.careerTitle}>{video.career.title}</Text>
        <Text style={styles.industry}>{video.career.industry_sector}</Text>
        <Text style={styles.description}>{video.career.description}</Text>
        <Text style={styles.salary}>{formatSalary()}</Text>
        <Text style={styles.education}>{video.career.education_required}</Text>
      </View>

      {/* Action buttons */}
      <View style={styles.actionsContainer}>
        <TouchableOpacity
          style={styles.actionButton}
          onPress={handleLike}
        >
          <Text style={styles.actionIcon}>{liked ? '❤️' : '🤍'}</Text>
          <Text style={styles.actionLabel}>Like</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.actionButton}
          onPress={handleSave}
        >
          <Text style={styles.actionIcon}>{saved ? '⭐' : '☆'}</Text>
          <Text style={styles.actionLabel}>Save</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.actionButton}
          onPress={handleShare}
        >
          <Text style={styles.actionIcon}>↗️</Text>
          <Text style={styles.actionLabel}>Share</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.actionButton}
          onPress={handleSkip}
        >
          <Text style={styles.actionIcon}>→</Text>
          <Text style={styles.actionLabel}>Skip</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    height,
    width,
    backgroundColor: '#000',
  },
  video: {
    height: '100%',
    width: '100%',
  },
  gradient: {
    position: 'absolute',
    left: 0,
    right: 0,
    bottom: 0,
    height: height * 0.5,
  },
  infoContainer: {
    position: 'absolute',
    bottom: 120,
    left: 20,
    right: 100,
  },
  careerTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 4,
  },
  industry: {
    fontSize: 16,
    color: '#A3A3A3',
    marginBottom: 8,
    fontWeight: '500',
  },
  description: {
    fontSize: 16,
    color: '#fff',
    marginBottom: 12,
    lineHeight: 22,
  },
  salary: {
    fontSize: 18,
    color: '#4ADE80',
    fontWeight: '600',
    marginBottom: 4,
  },
  education: {
    fontSize: 14,
    color: '#D1D5DB',
  },
  actionsContainer: {
    position: 'absolute',
    right: 12,
    bottom: 120,
    gap: 24,
  },
  actionButton: {
    alignItems: 'center',
  },
  actionIcon: {
    fontSize: 32,
    marginBottom: 4,
  },
  actionLabel: {
    fontSize: 12,
    color: '#fff',
    fontWeight: '500',
  },
});
