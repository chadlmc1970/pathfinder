import React, { useRef, useState } from 'react';
import { View, FlatList, Dimensions, StyleSheet } from 'react-native';
import VideoCard from '../components/VideoCard';

const { height } = Dimensions.get('window');

// Mock data - will connect to backend API
const MOCK_VIDEOS = [
  {
    id: '1',
    career_title: 'Software Engineer',
    video_url: 'https://placeholder.com/video1.mp4',
    thumbnail_url: 'https://placeholder.com/thumb1.jpg',
    description: 'Build apps and websites that millions of people use every day.',
    average_salary: 120000,
    education_required: "Bachelor's degree in Computer Science"
  },
  {
    id: '2',
    career_title: 'Nurse Practitioner',
    video_url: 'https://placeholder.com/video2.mp4',
    thumbnail_url: 'https://placeholder.com/thumb2.jpg',
    description: 'Provide medical care and improve patient health outcomes.',
    average_salary: 115000,
    education_required: "Master's degree in Nursing"
  }
];

export default function HomeScreen() {
  const [activeVideoIndex, setActiveVideoIndex] = useState(0);
  const flatListRef = useRef<FlatList>(null);

  const onViewableItemsChanged = useRef(({ viewableItems }: any) => {
    if (viewableItems.length > 0) {
      setActiveVideoIndex(viewableItems[0].index || 0);
    }
  }).current;

  const viewabilityConfig = useRef({
    itemVisiblePercentThreshold: 80,
  }).current;

  return (
    <View style={styles.container}>
      <FlatList
        ref={flatListRef}
        data={MOCK_VIDEOS}
        renderItem={({ item, index }) => (
          <VideoCard
            video={item}
            isActive={index === activeVideoIndex}
          />
        )}
        keyExtractor={(item) => item.id}
        pagingEnabled
        showsVerticalScrollIndicator={false}
        snapToInterval={height}
        snapToAlignment="start"
        decelerationRate="fast"
        onViewableItemsChanged={onViewableItemsChanged}
        viewabilityConfig={viewabilityConfig}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000',
  },
});
