import React, { useState } from 'react';
import { View, Text, StyleSheet, Dimensions, TouchableOpacity, Image } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';

const { height, width } = Dimensions.get('window');

interface VideoCardProps {
  video: {
    id: string;
    career_title: string;
    video_url: string;
    thumbnail_url: string;
    description: string;
    average_salary: number;
    education_required: string;
  };
  isActive: boolean;
}

export default function VideoCard({ video, isActive }: VideoCardProps) {
  const [liked, setLiked] = useState(false);
  const [saved, setSaved] = useState(false);

  return (
    <View style={styles.container}>
      {/* Video placeholder - will integrate expo-av for actual video */}
      <Image
        source={{ uri: video.thumbnail_url }}
        style={styles.video}
        resizeMode="cover"
      />

      {/* Gradient overlay */}
      <LinearGradient
        colors={['transparent', 'rgba(0,0,0,0.8)']}
        style={styles.gradient}
      />

      {/* Career info */}
      <View style={styles.infoContainer}>
        <Text style={styles.careerTitle}>{video.career_title}</Text>
        <Text style={styles.description}>{video.description}</Text>
        <Text style={styles.salary}>
          Average Salary: ${(video.average_salary / 1000).toFixed(0)}K/year
        </Text>
        <Text style={styles.education}>{video.education_required}</Text>
      </View>

      {/* Action buttons */}
      <View style={styles.actionsContainer}>
        <TouchableOpacity
          style={styles.actionButton}
          onPress={() => setLiked(!liked)}
        >
          <Text style={styles.actionIcon}>{liked ? '❤️' : '🤍'}</Text>
          <Text style={styles.actionLabel}>Like</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.actionButton}
          onPress={() => setSaved(!saved)}
        >
          <Text style={styles.actionIcon}>{saved ? '⭐' : '☆'}</Text>
          <Text style={styles.actionLabel}>Save</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.actionButton}>
          <Text style={styles.actionIcon}>↗️</Text>
          <Text style={styles.actionLabel}>Share</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.actionButton}>
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
    marginBottom: 8,
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
