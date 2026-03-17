import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  FlatList,
  TouchableOpacity,
  ActivityIndicator,
  SafeAreaView,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { getRecommendations, Recommendation, Career } from '../services/api';
import { useRouter } from 'expo-router';

export default function RecommendationsScreen() {
  const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  useEffect(() => {
    loadRecommendations();
  }, []);

  const loadRecommendations = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await getRecommendations(10);
      setRecommendations(data);
    } catch (err) {
      console.error('Failed to load recommendations:', err);
      setError('Failed to load AI recommendations. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const renderRecommendation = ({ item, index }: { item: Recommendation; index: number }) => {
    const career = item.career;
    if (!career) return null;

    const formatSalary = () => {
      if (career.salary_range_min && career.salary_range_max) {
        return `$${(career.salary_range_min / 1000).toFixed(0)}K-$${(career.salary_range_max / 1000).toFixed(0)}K`;
      } else if (career.salary_range_min) {
        return `$${(career.salary_range_min / 1000).toFixed(0)}K+`;
      }
      return 'Varies';
    };

    const matchPercentage = Math.round(item.score);

    return (
      <TouchableOpacity style={styles.card} activeOpacity={0.8}>
        <LinearGradient
          colors={['#1F2937', '#111827']}
          style={styles.cardGradient}
        >
          {/* Match badge */}
          <View style={styles.matchBadge}>
            <Text style={styles.matchText}>{matchPercentage}% Match</Text>
          </View>

          {/* Rank */}
          <View style={styles.rankBadge}>
            <Text style={styles.rankText}>#{index + 1}</Text>
          </View>

          {/* Career info */}
          <Text style={styles.careerTitle}>{career.title}</Text>
          <Text style={styles.industry}>{career.industry_sector}</Text>

          {/* Salary */}
          <View style={styles.salaryContainer}>
            <Text style={styles.salaryLabel}>Average Salary: </Text>
            <Text style={styles.salary}>{formatSalary()}/year</Text>
          </View>

          {/* Education */}
          <View style={styles.educationContainer}>
            <Text style={styles.educationIcon}>🎓</Text>
            <Text style={styles.education}>{career.education_required}</Text>
          </View>

          {/* AI reasoning */}
          <View style={styles.reasonContainer}>
            <Text style={styles.reasonLabel}>Why this matches you:</Text>
            <Text style={styles.reason}>{item.reason}</Text>
          </View>

          {/* Skills preview */}
          {career.skills && career.skills.length > 0 && (
            <View style={styles.skillsContainer}>
              {career.skills.slice(0, 3).map((skill, idx) => (
                <View key={idx} style={styles.skillPill}>
                  <Text style={styles.skillText}>{skill}</Text>
                </View>
              ))}
              {career.skills.length > 3 && (
                <Text style={styles.moreSkills}>+{career.skills.length - 3} more</Text>
              )}
            </View>
          )}

          {/* CTA button */}
          <TouchableOpacity style={styles.exploreButton}>
            <Text style={styles.exploreButtonText}>Explore This Career</Text>
          </TouchableOpacity>
        </LinearGradient>
      </TouchableOpacity>
    );
  };

  if (loading) {
    return (
      <View style={[styles.container, styles.centered]}>
        <ActivityIndicator size="large" color="#4ADE80" />
        <Text style={styles.loadingText}>Loading AI recommendations...</Text>
      </View>
    );
  }

  if (error) {
    return (
      <View style={[styles.container, styles.centered]}>
        <Text style={styles.errorText}>{error}</Text>
        <TouchableOpacity style={styles.retryButton} onPress={loadRecommendations}>
          <Text style={styles.retryText}>Retry</Text>
        </TouchableOpacity>
      </View>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.back()} style={styles.backButton}>
          <Text style={styles.backIcon}>←</Text>
        </TouchableOpacity>
        <View style={styles.headerTextContainer}>
          <Text style={styles.headerTitle}>AI Recommendations</Text>
          <Text style={styles.headerSubtitle}>
            Careers matched to your interests
          </Text>
        </View>
      </View>

      {/* Recommendations list */}
      <FlatList
        data={recommendations}
        renderItem={renderRecommendation}
        keyExtractor={(item) => item.id.toString()}
        contentContainerStyle={styles.listContent}
        showsVerticalScrollIndicator={false}
        ListEmptyComponent={
          <View style={styles.emptyContainer}>
            <Text style={styles.emptyText}>
              No recommendations yet. Start exploring careers to get personalized suggestions!
            </Text>
          </View>
        }
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000',
  },
  centered: {
    justifyContent: 'center',
    alignItems: 'center',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#1F2937',
  },
  backButton: {
    padding: 8,
  },
  backIcon: {
    fontSize: 24,
    color: '#fff',
  },
  headerTextContainer: {
    marginLeft: 12,
    flex: 1,
  },
  headerTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
  },
  headerSubtitle: {
    fontSize: 14,
    color: '#9CA3AF',
    marginTop: 2,
  },
  listContent: {
    padding: 16,
  },
  card: {
    marginBottom: 16,
    borderRadius: 16,
    overflow: 'hidden',
  },
  cardGradient: {
    padding: 20,
    borderWidth: 1,
    borderColor: '#374151',
    borderRadius: 16,
  },
  matchBadge: {
    position: 'absolute',
    top: 16,
    right: 16,
    backgroundColor: '#4ADE80',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 20,
  },
  matchText: {
    color: '#000',
    fontSize: 14,
    fontWeight: '700',
  },
  rankBadge: {
    position: 'absolute',
    top: 16,
    left: 16,
    backgroundColor: '#374151',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
  },
  rankText: {
    color: '#9CA3AF',
    fontSize: 12,
    fontWeight: '600',
  },
  careerTitle: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#fff',
    marginTop: 40,
    marginBottom: 4,
  },
  industry: {
    fontSize: 14,
    color: '#9CA3AF',
    marginBottom: 16,
    fontWeight: '500',
  },
  salaryContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  salaryLabel: {
    fontSize: 14,
    color: '#D1D5DB',
  },
  salary: {
    fontSize: 16,
    color: '#4ADE80',
    fontWeight: '600',
  },
  educationContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 16,
  },
  educationIcon: {
    fontSize: 16,
    marginRight: 6,
  },
  education: {
    fontSize: 14,
    color: '#D1D5DB',
    flex: 1,
  },
  reasonContainer: {
    backgroundColor: '#111827',
    padding: 12,
    borderRadius: 12,
    marginBottom: 16,
  },
  reasonLabel: {
    fontSize: 12,
    color: '#9CA3AF',
    marginBottom: 6,
    fontWeight: '600',
  },
  reason: {
    fontSize: 14,
    color: '#fff',
    lineHeight: 20,
  },
  skillsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
    marginBottom: 16,
  },
  skillPill: {
    backgroundColor: '#374151',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 16,
  },
  skillText: {
    fontSize: 12,
    color: '#D1D5DB',
    fontWeight: '500',
  },
  moreSkills: {
    fontSize: 12,
    color: '#9CA3AF',
    alignSelf: 'center',
  },
  exploreButton: {
    backgroundColor: '#4ADE80',
    paddingVertical: 12,
    borderRadius: 12,
    alignItems: 'center',
  },
  exploreButtonText: {
    color: '#000',
    fontSize: 16,
    fontWeight: '600',
  },
  loadingText: {
    color: '#fff',
    fontSize: 16,
    marginTop: 12,
  },
  errorText: {
    color: '#fff',
    fontSize: 16,
    textAlign: 'center',
    marginBottom: 16,
    paddingHorizontal: 20,
  },
  retryButton: {
    backgroundColor: '#4ADE80',
    paddingHorizontal: 24,
    paddingVertical: 12,
    borderRadius: 12,
  },
  retryText: {
    color: '#000',
    fontSize: 16,
    fontWeight: '600',
  },
  emptyContainer: {
    padding: 40,
    alignItems: 'center',
  },
  emptyText: {
    color: '#9CA3AF',
    fontSize: 16,
    textAlign: 'center',
    lineHeight: 24,
  },
});
